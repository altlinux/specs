Name: python3-module-construct
Version: 2.10.56
Release: alt1

Summary: A powerful declarative parser/builder for binary data
License: MIT
Group: Development/Python
Url: https://pypi.org/project/construct/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
Construct is a powerful declarative parser (and builder) for binary
data.

Instead of writing imperative code to parse a piece of data, you
declaratively define a data structure that describes your data. As
this data structure is not code, you can use it in one direction to
parse data into Pythonic objects, and in the other direction, convert
(build) objects into binary data.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.rst LICENSE
%python3_sitelibdir/construct
%python3_sitelibdir/construct-%version-*-info

%changelog
* Fri Jul 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.10.56-alt1
- 2.10.56 released

* Mon Dec 12 2016 Lenar Shakirov <snejok@altlinux.ru> 2.5.1-alt1
- Initial build for ALT (based on 2.5.1-8.fc25.src)
