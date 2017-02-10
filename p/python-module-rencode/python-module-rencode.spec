%define oname rencode

%def_with python3

Name: python-module-%oname
Version: 1.0.5
Release: alt1

Summary: The rencode module is similar to bencode from the BitTorrent project

Group: Development/Python
License: LGPL
Url: https://pypi.python.org/pypi/rencod

Packager: Vitaly Lipatov <lav@altlinux.ru>

%setup_python_module %oname

# Source-url: https://github.com/aresch/rencode/archive/v%version.tar.gz
Source: %name-%version.tar

%if_with python3
BuildRequires(pre): rpm-build-python3
%endif

# manually removed:  python3-module-zope ruby ruby-stdlibs
# Automatically added by buildreq on Sat Apr 23 2016
# optimized out: python-base python-devel python-module-distribute python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-json python-modules-xml python3 python3-base
BuildRequires: python-module-Cython python-module-PyXML python-module-google python-module-mwlib python3-dev python3-module-Cython

%description
The rencode module is similar to bencode from the BitTorrent project.
Forcomplex, heterogeneous data structures with many small elements,
r-encodingstake up significantly less space than b-encodings.
This version of rencode isa complete rewrite in Cython to attempt
to increase the performance over thepure Python module
written by Petru Paler, Connelly Barnes et al.

%package -n python3-module-%oname
Summary: The rencode module is similar to bencode from the BitTorrent project
Group: Development/Python3

%description -n python3-module-%oname
The rencode module is similar to bencode from the BitTorrent project.
Forcomplex, heterogeneous data structures with many small elements,
r-encodingstake up significantly less space than b-encodings.
This version of rencode isa complete rewrite in Cython to attempt
to increase the performance over thepure Python module
written by Petru Paler, Connelly Barnes et al.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing

%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%files
%python_sitelibdir/*
#_docdir/%modulename/

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 10 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt1
- new version 1.0.5 (with rpmrb script)

* Sat Apr 23 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- initial build for ALT Linux Sisyphus
