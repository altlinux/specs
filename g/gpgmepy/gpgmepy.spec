%define _unpackaged_files_terminate_build 1
%add_python3_req_skip _gpgme

Name: gpgmepy
Version: 2.0.0
Release: alt1

Summary: Python bindings for GPGME
License: LGPLv2.1+
Group: Development/Python
Url: https://www.gnupg.org/software/gpgme/index.html
Vcs: git://git.gnupg.org/gpgmepy.git

Source: %name-%version.tar
Patch1: alt-copy-files.patch
# SuSE
Patch100: python-gpg-nobetasuffix.patch
Patch101: gpgmepy-2.0.0-swig-32-bit.patch
Patch102: build-pep621-pyproject.patch

BuildRequires(pre): python3-devel python3(setuptools)
BuildRequires: gnupg2 swig gpgme2-devel libgpg-error-devel

%package -n python3-module-gpg
Summary: Python GPGME bindings
Group: Development/Python

%description -n python3-module-gpg
Python bindings for GPGME.

%description
Python bindings for GPGME.

%prep
%setup
%patch1 -p1
#
%patch100 -p1
%patch101 -p1
%patch102 -p1
%autoreconf
ln -sf ./src gpg

%build
%if "%_lib" == "lib"
%add_optflags -D_FILE_OFFSET_BITS=64
%endif
%configure
%make_build GPG=gpg2

%install
%make install-am DESTDIR=%buildroot prefix=%_prefix

# Keep only PKG-INFO and *.txt files in egg-info dirs.
find %buildroot/%python3_sitelibdir/gpg-%version-py*egg-info \
     -mindepth 1 -maxdepth 1 \
     ! -name  'PKG-INFO' -a ! -name '*.txt' \
     -delete ||:

%files -n python3-module-gpg
%python3_sitelibdir/gpg-%version-py*egg-info
%dir %python3_sitelibdir/gpg
%python3_sitelibdir/gpg/*

%changelog
* Fri Jul 10 2026 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt1
- initial build
