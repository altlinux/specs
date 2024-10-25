Group: Text tools
%define _localstatedir %{_var}
%define lang ru
%define langrelease 1
%define aspellversion 6
Summary: GNU Aspell Russian Word List Package
Name: aspell-%{lang}
Version: 0.99f7
Release: alt1
License: MIT and BSD
URL: http://aspell.net/
Source: ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell%{aspellversion}-%{lang}-%{version}-%{langrelease}.tar.bz2
Buildrequires: aspell libaspell
Requires: aspell libaspell

%define debug_package %{nil}

%description
GNU Aspell Russian Word List Package

%prep
%setup -q -n aspell%{aspellversion}-%{lang}-%{version}-%{langrelease}

%build
./configure
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc Copyright
%{_libdir}/aspell/*
%{_datadir}/aspell/*

%changelog
* Fri Oct 25 2024 Alexei Takaseev <taf@altlinux.org> 0.99f7-alt1
- 0.99f7

* Mon Oct 20 2003 Vital Khilko <vk@altlinux.ru> 0.50-alt2
- fix dependencies

* Tue Sep 16 2003 Vital Khilko <vk@altlinux.ru> 0.50-alt1
- New official package from aspell.net
