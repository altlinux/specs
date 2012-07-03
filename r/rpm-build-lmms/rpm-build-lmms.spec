Name: rpm-build-lmms
Version: 0.1
Release: alt1

Summary: Helper package for creation of build dependences lmms
License: GPL
Group: Development/Other

Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

%ifarch %ix86
Requires: libwine-devel
%endif

%description
Helper package for creation of build dependences for lmms

%files

%changelog
* Tue Dec 11 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1-alt1
- initial build
