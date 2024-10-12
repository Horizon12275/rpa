package com.rpa.backend.config;


import com.rpa.backend.interceptor.SessionInterceptor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class SessionConfiguration implements WebMvcConfigurer {
    private final SessionInterceptor sessionInterceptor;

    @Autowired
    public SessionConfiguration(SessionInterceptor sessionInterceptor) {
        this.sessionInterceptor = sessionInterceptor;
    }

    //注册拦截器，添加拦截路径和排除拦截路径，InterceptorRegistry 是用于注册拦截器的类
    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(sessionInterceptor)
//                .addPathPatterns("/**")
                .excludePathPatterns("/**")
                .excludePathPatterns("/ws/**")
                .excludePathPatterns("/api/user/login")
                .excludePathPatterns("/swagger-ui/**")
                .excludePathPatterns("/api-docs");
    }

    //所有情况下都允许 CORS 请求，CorsRegistry 是用于配置 CORS 请求的类
    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**")
                .allowCredentials(true)
                .allowedOriginPatterns("*")
                .allowedMethods("*")
                .allowedHeaders("*")
                .exposedHeaders("*");
    }
}
