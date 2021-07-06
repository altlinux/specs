%define _unpackaged_files_terminate_build 1

%define oname yelp_encodings

Name:           python3-module-yelp-encodings
Version:        1.0.0
Release:        alt1
Summary:        String encodings invented and maintained by yelp.
Group:          Development/Python3
License:        Unlicense
URL:            https://pypi.python.org/pypi/yelp_encodings

BuildArch:      noarch

# https://github.com/Yelp/yelp_encodings.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3(pytest)

%description
yelp_encodings contains an 'internet' encoding which is appropriate
for dealing with poorly encoded bytes coming from internet clients.
The internet encoding will always succeed in decoding any bytestring.
This is most often useful for logging bad requests.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test

%files
%doc UNLICENSE
%doc README.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py3*.egg-info

%changelog
* Tue Jul 06 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt1
- Updated to upstream version 1.0.0.
- Disabled building module for python-2.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt2.qa1
- NMU: applied repocop patch

* Thu Mar 01 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.3-alt2
- Updated build dependencies.

* Wed Oct 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.3-alt1
- Initial build for ALT.
