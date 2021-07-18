%define _unpackaged_files_terminate_build 1
%define oname lexicon

%def_with check

Name: python3-module-%oname
Version: 1.0.0
Release: alt2

Summary: Powerful Python dict subclass(es) providing aliasing & attribute access
License: BSD-2-Clause
Group: Development/Python3
Url: https://github.com/bitprophet/lexicon

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-six
%endif


%description
Lexicon is a simple Python 2.6+ and 3.3+ compatible collection of dict subclasses
providing extra power.


%prep
%setup

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc LICENSE README.md CHANGES
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info


%changelog
* Sun Jul 18 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- drop tests packing (the tests is not used by other packages)

* Tue Feb 18 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.0-alt1
- Initial build.

