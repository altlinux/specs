%define _unpackaged_files_terminate_build 1
%define oname libfaketime

Name: python3-module-libfaketime
Version: 2.0.0
Release: alt1

Summary: A fast alternative to freezegun that wraps libfaketime

License: GPLv2
Group: Development/Python3
Url: https://pypi.org/project/libfaketime/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

Requires: libfaketime >= 0.9.9

%description
python-libfaketime is a wrapper of libfaketime for python. Some brief details:

* Mostly compatible with freezegun.
* Microsecond resolution.
* Accepts datetimes and strings that can be parsed by dateutil.
* Not threadsafe.


%prep
%setup
# use system library
subst "s|: _get_lib_path()|: '%_libdir/faketime'|" libfaketime/__init__.py

%build
%python3_build_debug

%install
%python3_install

# FIXME
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

# use system library
rm -rv %buildroot%python3_sitelibdir/libfaketime/vendor/


%files
%doc *.rst
%_bindir/python-libfaketime
%python3_sitelibdir/*


%changelog
* Mon Sep 06 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- initial build for ALT Sisyphus

