# packaged formats
%define formats text json html template

Name: license-list-data
Version: 3.25.0
Release: alt1

Summary: License List Data
License: CC-BY-3.0
Group: System/Base
Url: https://github.com/spdx/license-list-data

Vcs: https://github.com/spdx/license-list-data.git

Source: https://github.com/spdx/license-list-data/archive/v%version/%name-%version.tar.gz

BuildArch: noarch
AutoReqProv: no

%description
This package contains various generated data formats for the SPDX
License List including RDFa, HTML, Text, and JSON. The source of the
license list which generates these data files can be found at
https://github.com/spdx/license-list-XML.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/%name
for dir in %formats; do
    cp -ar $dir %buildroot%_datadir/%name/$dir
done

%files
%_datadir/%name/
%doc *.md

%changelog
* Wed Oct 23 2024 Yuri N. Sedunov <aris@altlinux.org> 3.25.0-alt1
- first build for Sisyphus.
