%def_disable check

Version: 2.0.82
Release: alt1.1
%setup_python_module sepolgen
Name: python-module-sepolgen
Summary: A Python module used in SELinux policy generation
License: %gpl2plus
Group: Development/Python
Source: %modulename-%version.tar
Url: http://userspace.selinuxproject.org/trac/
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses
BuildPreReq: python-module-selinux 

%if_enabled check
BuildPreReq: selinux-policy
%endif

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
make test

%files
%python_sitelibdir/*
/var/lib/sepolgen/

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.82-alt1.1
- Rebuild with Python-2.7

* Thu Aug 26 2010 Mikhail Efremov <sem@altlinux.org> 2.0.82-alt1
- Separate from policycoreutils

