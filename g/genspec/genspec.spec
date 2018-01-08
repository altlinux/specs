Name:     genspec
Version:  1.2.15
Release:  alt1

Summary:  Script for generation RPM spec file from template
License:  GPLv3+
Group:    System/Configuration/Packaging
URL:      http://altlinux.org/genspec
Packager: Andrey Cherepanov <cas@altlinux.org>

BuildArch: noarch

BuildPrereq: rpm-build-python3

Requires: git-core gear perl-Gear-Remotes

Source:   %name-%version.tar

%description
Script for generation RPM spec file from template.

%prep
%setup

%install
install -Dm755 %name %buildroot%_bindir/%name
mkdir -p %buildroot%_datadir/spectemplates
cp -av spectemplates/* %buildroot%_datadir/spectemplates/

%files
%_bindir/%name
%_datadir/spectemplates

%changelog
* Mon Jan 08 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.15-alt1
- Add readline
- Create golang-bin spectemplate
- Add owner option

* Fri Oct 20 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.14-alt1
- Fix interactive mode broken with last update

* Thu Oct 19 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.13-alt1
- (ALT #34017) Use deafult value for optional arguments

* Mon Oct 16 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.12-alt1
- Replace tabs with whitespaces

* Thu Sep 28 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.11-alt1
- (ALT #33935) Print created directory

* Fri Sep 01 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.10-alt1
- Add newline to generating .gear/rules
- Fail if could not get packager

* Wed Aug 02 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.9-alt1
- Add new spectemplates for executables

* Thu Jul 06 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.8-alt1
- Add test option

* Wed Jul 05 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.7-alt1
- Fix using gear post operations without --git option

* Wed Jun 28 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.6-alt1
- Create python3 spectemplate

* Tue Jun 27 2017 Gordeev Mikhail <obirvalger@altlinux.org> 1.2.5-alt1
- (ALT #33596): wrong syntax for building from tag

* Tue Jun 20 2017 Gordeev Mikhail <obirvalger@altlinux.org> 1.2.4-alt1
- Add git command line option to clone from url, clear repo and configure
  gear remotes update (currently doesn't handle git error: no internet
  connection and not configured git)

* Mon Jun 19 2017 Gordeev Mikhail <obirvalger@altlinux.org> 1.2.2-alt1
- Add tag command line option (uses in .gear/rules)

* Tue May 16 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.0-alt1
- Split in two packages: genspec and github2spec

* Tue May 16 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.2-alt1
- Fix several issues

* Thu May 11 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.1-alt2
- Add rpm-build-ruby rpm-build-python3 to BuildPrereq

* Thu May 11 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.1-alt1
- Fix invocation of ./genspec instead of genspec

* Thu May 11 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.0-alt1
- Create script to get repository data from github and generate spec file

* Tue May 2 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.2-alt1
- Upgrade to python3

* Mon Apr 24 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.1-alt1
- Add interactive mode

* Fri Jan 30 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial publish
