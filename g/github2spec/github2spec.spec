Name:     github2spec
Version:  1.3.4
Release:  alt1

Summary:  Script for generation RPM spec file from github using genspec
License:  GPLv3+
Group:    System/Configuration/Packaging
URL: 	  http://altlinux.org/genspec
Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildArch: noarch

BuildPrereq: rpm-build-ruby

Requires: genspec >= 1.2.2

Source:   %name-%version.tar

%description
Script to get repository data from github and generate RPM spec file with
genspec. Program works in interactive mode, only one required value is URL.
Then you insert URL, the program will ask you to enter another values, but
before asking it would suggest default value. If you accept it then just press
Enter.

%prep
%setup

%install
install -Dm755 %name %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Mon Jun 19 2017 Gordeev Mikhail <obirvalger@altlinux.org> 1.3.4-alt1
- Pass tag to genspec

* Wed Jun 14 2017 Gordeev Mikhail <obirvalger@altlinux.org> 1.3.2-alt1
- Fix faults with missing description and tags

* Thu Jun 01 2017 Gordeev Mikhail <obirvalger@altlinux.org> 1.3.1-alt1
- Add command line options to control interactive level
- Fix issue with nil license
- Fix issue with quoting in data from github

* Tue May 16 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.0-alt1
- Initial build as separate package (before it was part of genspec)
