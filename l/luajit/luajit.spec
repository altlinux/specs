Name: luajit
Version: 2.0
Release: alt1
License: MIT
Url: http://luajit.org
Source: %name-%version.tar
Group: Development/Other
Summary: a Just-In-Time Compiler for Lua
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

#BuildRequires:

%description
LuaJIT is a Just-In-Time Compiler (JIT) for the Lua programming language. 
Lua is a powerful, dynamic and light-weight programming language. 
It may be embedded or used as a general-purpose, stand-alone language.

%package -n lib%name
Summary: library for luajit
Group: Development/Other

%description -n lib%name
LuaJIT is a Just-In-Time Compiler (JIT) for the Lua programming language. 
Lua is a powerful, dynamic and light-weight programming language. 
It may be embedded or used as a general-purpose, stand-alone language.

%package -n lib%name-devel
Summary:  Development package that includes the luajit header files
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
LuaJIT is a Just-In-Time Compiler (JIT) for the Lua programming language. 
Lua is a powerful, dynamic and light-weight programming language. 
It may be embedded or used as a general-purpose, stand-alone language.

%package -n lib%name-devel-static
Summary: static library for luajit
Group: System/Libraries
        
%description -n lib%name-devel-static
LuaJIT is a Just-In-Time Compiler (JIT) for the Lua programming language. 
Lua is a powerful, dynamic and light-weight programming language. 
It may be embedded or used as a general-purpose, stand-alone language.

%prep
%setup

%build
%make amalg PREFIX=%_prefix

%install
%makeinstall_std PREFIX=%_prefix LDCONFIG=true INSTALL_LIB=%buildroot%_libdir


%files
%_bindir/*
%_datadir/%name-*
%_man1dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%doc doc/*
%_libdir/*.so
%_includedir/%name-%version
%_pkgconfigdir/*

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Sun Dec 16 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0-alt1
- Buld for ALT
