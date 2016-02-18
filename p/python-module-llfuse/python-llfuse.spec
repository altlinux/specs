# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-build-python3 rpm-macros-fedora-compat
# END SourceDeps(oneline)
%define oldname python-llfuse
%define fedora 21
%if 0%{?fedora} > 12 || 0%{?rhel} > 6
%global with_python3 1
%else
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}
%endif

%if 0%{?with_python3}

%endif # if with_python3

Name: python-module-llfuse
Version: 0.40
Release: alt1_4.1

Summary: Python Bindings for the low-level FUSE API

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://python-llfuse.googlecode.com/files/llfuse-%version.tar.bz2
Url: http://code.google.com/p/python-llfuse/
Group: Development/Python
License: LGPLv2+

BuildRequires(pre): rpm-macros-fedora-compat
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils pkg-config python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: libattr-devel libfuse-devel python-module-setuptools python3-devel python3-module-setuptools rpm-build-python3

#BuildRequires: libattr-devel
#BuildRequires: libfuse-devel >= 2.8.0
#BuildRequires: python-module-setuptools
#BuildRequires: python-devel
%if 0%{?with_python3}
#BuildRequires: python3-devel
#BuildRequires: python3-module-distribute
%endif # if with_python3
Source44: import.info
%add_findprov_skiplist %python_sitelibdir/.*\.so$
%add_findprov_skiplist %python3_sitelibdir/.*\.so$

%description
LLFUSE is a set of Python bindings for the low level FUSE API. It requires at
least FUSE 2.8.0.

LLFUSE was originally part of S3QL, but has been factored out so that it can be
used by other projects as well.
%if 0%{?with_python3}
%package -n python3-module-llfuse
Summary: Python Bindings for the low-level FUSE API Python 3 packages
Group: Development/Python

%description -n python3-module-llfuse
LLFUSE is a set of Python 3 bindings for the low level FUSE API. It requires at
least FUSE 2.8.0.

LLFUSE was originally part of S3QL, but has been factored out so that it can be
used by other projects as well.
%endif # with_python3

%prep
%setup -n "llfuse-%version"
rm doc/html/.buildinfo
rm -rf src/llfuse.egg-info

%if 0%{?with_python3}
rm -rf %_builddir/python3-%oldname-%version-%release
cp -a . %_builddir/python3-%oldname-%version-%release
find %_builddir/python3-%oldname-%version-%release -name '*.py' | xargs sed -i '1s|^#!python|#!%__python3|'
%endif # with_python3
find -name '*.py' | xargs sed -i '1s|^#!python|#!%__python|'

%build
%python_build

%if 0%{?with_python3}
pushd %_builddir/python3-%oldname-%version-%release
CFLAGS="$RPM_OPT_FLAGS" %__python3 setup.py build
popd
%endif # with_python3

%install
%if 0%{?with_python3}
pushd %_builddir/python3-%oldname-%version-%release
%__python3 setup.py install --root %buildroot
popd
%endif # with_python3

%python_install

%files
%doc Changes.txt doc/html LICENSE
%python_sitelibdir/*
%if 0%{?with_python3}
%files -n python3-module-llfuse
%doc Changes.txt doc/html LICENSE
%python3_sitelibdir/*
%endif # with_python3

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.40-alt1_4.1
- NMU: Use buildreq for BR.

* Fri Aug 14 2015 Vitaly Lipatov <lav@altlinux.ru> 0.40-alt1_4
- human build for ALT Linux Sisyphus

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1_3
- update to new release by fcimport

* Thu Jan 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1_1
- update to new release by fcimport

* Mon Feb 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_1
- update to new release by fcimport

* Wed Jan 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.37.1-alt1_11
- initial fc import

