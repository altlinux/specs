%def_disable check

Name: python-module-sepolgen
Version: 1.2.2
Release: alt1
Epoch: 2
%setup_python_module sepolgen
Summary: A Python module used in SELinux policy generation
License: GPL2+
Group: Development/Python
Source: %modulename-%version.tar
Url: http://userspace.selinuxproject.org
BuildArch: noarch
Provides: %modulename = %version-%release

BuildPreReq: rpm-build-python
BuildRequires: python-module-selinux
%{!?_disable_check:BuildPreReq: selinux-policy}


%description
This package contains a Python module that forms the core of the modern
audit2allow (which is a part of the package policycoreutils).
The sepolgen library is structured to give flexibility to the
application using it. The library contains: Reference Policy
Representation, which are Objects for representing policies and the
reference policy interfaces. Secondly, it has objects and algorithms for
representing access and sets of access in an abstract way and searching
that access. It also has a parser for reference policy "headers". It
contains infrastructure for parsing SELinux related messages as produced
by the audit system. It has facilities for generating policy based on
required access.


%prep
%setup -n %modulename-%version


%install
%makeinstall_std PYTHONLIBDIR=%python_sitelibdir


%check
%make_build test


%files
%python_sitelibdir/*
/var/lib/sepolgen/


%changelog
* Wed Feb 10 2016 Sergey V Turchin <zerg@altlinux.org> 2:1.2.2-alt1
- new version

* Tue Jan 21 2014 Andriy Stepanov <stanv@altlinux.ru> 2:1.2.1-alt1
- new version

* Tue Nov 19 2013 Anton Farygin <rider@altlinux.ru> 1:2.0.82-alt1
- new version

* Thu Jun 27 2013 Andriy Stepanov <stanv@altlinux.ru> 1:1.1.9-alt1
- New version

* Sun Sep 23 2012 Led <led@altlinux.ru> 1:1.1.8-alt1
- 1.1.8
- cleaned up spec

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.82-alt1.1
- Rebuild with Python-2.7

* Thu Aug 26 2010 Mikhail Efremov <sem@altlinux.org> 2.0.82-alt1
- Separate from policycoreutils

