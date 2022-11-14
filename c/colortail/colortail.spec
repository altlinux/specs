%def_enable check

Name: colortail
Version: 0.3.4
Release: alt0.5

Summary: A colorised tail with configuration files
License: GPL-2.0
Group: Monitoring

Url: https://github.com/joakim666/colortail
%if_disabled snapshot
Source: %url/releases/download/%version/%name-%version.tar.gz
%else
Vcs: https://github.com/joakim666/colortail.git
Source: %name-%version.tar
%endif

BuildRequires: gcc-c++

%description
Colortail is a log colorizer make log checking easier.
It works like tail but can read one or more configuration files.
In which it's specified which patterns result in which colors.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
install -d %buildroot/%_sysconfdir/%name
install -pm644 example-conf/conf* %buildroot/%_sysconfdir/%name

%check
%make check

%files
%_bindir/%name
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%doc INSTALL README AUTHORS ChangeLog BUGS TODO

%changelog
* Tue Apr 19 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.4-alt0.5
- updated to 0.3.3-22-gad3bc53 (new GitHub homepage)

* Mon Jul 13 2020 Michael Shigorin <mike@altlinux.org> 0.3.3-alt1
- initial build for ALT Sisyphus (thx rosa)

* Fri Jul 25 2014 Denis Silakov <denis.silakov@rosalab.ru> 0.3.3-2
+ Revision: 0c968fa
- MassBuild#464: Increase release tag


