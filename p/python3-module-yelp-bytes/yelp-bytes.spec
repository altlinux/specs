%define _unpackaged_files_terminate_build 1

%define oname yelp_bytes

Name:           python3-module-yelp-bytes
Version:        0.3.0
Release:        alt3
Summary:        Utilities for dealing with byte strings, invented and maintained by Yelp.
Group:          Development/Python3
License:        Unlicense
URL:            https://pypi.python.org/pypi/yelp_bytes
BuildArch:      noarch

# https://github.com/Yelp/yelp_bytes.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3(yelp_encodings)
BuildRequires: python3(pytest)

%description
yelp_bytes contains several utility functions to help ensure
that the data you're using is always either Unicode or byte strings,
taking care of the edge cases for you so that you don't have to worry about them.
We handle ambiguous bytestrings by leveraging our our "internet" encoding.
This allows you to write functions that need unicode but can accept arbitrary values without crashing.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
py.test3

%files
%doc UNLICENSE
%doc README.md
%python3_sitelibdir/%{oname}.py
%python3_sitelibdir/__pycache__/%{oname}.*
%python3_sitelibdir/%oname-%version-py3*.egg-info

%changelog
* Tue Jul 06 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.0-alt3
- Rebuilt without python-2 support.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt2.qa1
- NMU: applied repocop patch

* Thu Mar 01 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.0-alt2
- Updated build dependencies.

* Wed Oct 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.0-alt1
- Initial build for ALT.
