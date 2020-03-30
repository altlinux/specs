Name: webtech
Version: 1.2.7
Release: alt1

Summary: A tool to identify technologies used on websites

License: GPLv3+
Group: Development/Python
Url: https://github.com/ShielderSec/webtech

Packager: Maxim Knyazev <mattaku@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%description
WebTech is a Python software that can identify web technologies by visiting
a given website, parsing a single response file or replaying a request
described in a text file. This way you can have reproducible results and
minimize the requests you need to make to a target website.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.md LICENSE
%_bindir/%name
%python3_sitelibdir/%name-*.egg-info/
%python3_sitelibdir/%name/

%changelog
* Mon Mar 30 2020 Maxim Knyazev <mattaku@altlinux.org> 1.2.7-alt1
- Initial build to Sisyphus
