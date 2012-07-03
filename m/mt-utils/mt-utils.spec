Name: mt-utils
Version: 0.0.1
Release: alt4.1

Summary: multitran command line utilities
License: LGPL
Group: System/Libraries

Source: %name-%{version}alpha3.tar.bz2
Patch: mt-utils-0.0.1-alt-DSO.patch

Requires: multitran-dict
Requires: libmtquery >= 0.0.1-alt3
BuildPreReq: libmtquery-devel >= 0.0.1-alt3

# Automatically added by buildreq on Fri Nov 12 2004
BuildRequires: gcc-c++ help2man libbtree-devel libfacet-devel libmtquery-devel libmtsupport-devel libstdc++-devel

%description
multitran utils:
 mtquery - utility for translating words and phrases
 
%prep
%setup -q -n %name-%{version}alpha3
%patch -p2

%build
%make_build

%install
%makeinstall DESTDIR=$RPM_BUILD_ROOT

%files
%doc ChangeLog
%_bindir/*
%_man1dir/*


%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt4.1
- Fixed build

* Fri Mar 10 2006 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt4
- fixed linking
- fixed work in utf8

* Mon Jan 24 2005 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt3
- alpha3

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.0.1-alt2.1
- Rebuilt with libstdc++.so.6.

* Thu Jan 13 2005 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt2
- alpha2

* Fri Nov 12 2004 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt1
- Initial build


