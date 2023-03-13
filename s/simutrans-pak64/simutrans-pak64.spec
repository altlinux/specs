Name: simutrans-pak64
Version: 123.0
Release: alt1
Summary: Transport and Economic Simulation Game Assets
License: Artistic-1.0
Group: Games/Strategy
Url: http://sourceforge.net/projects/simutrans/
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: http://downloads.sourceforge.net/simutrans/simupak64-123-0.zip
# or is the link this: https://downloads.sourceforge.net/project/simutrans/pak64/123-0/simupak64-123-0.zip
Source1: http://downloads.sourceforge.net/simutrans/simupak64-addon-food-120-4.zip
BuildRequires: fdupes
BuildRequires: unzip
Requires: simutrans >= 123.0
BuildArch: noarch

%description
Pak64 is the main and a base set for Simutrans developed along with Simutrans executable.
It always contains the most recent features. It is neatly painted pixel by pixel with
motherly care. On the other hand it might look too tiny on high resolution displays.
Many artists contributed to this pak set, from the 8 bit age on.
The optional food chain is included.

%prep
%setup -c -n simutrans
%setup -T -D -a 1 -c -n simutrans

%build
%install
mkdir -p %buildroot%_datadir/simutrans
cp -a simutrans/* %buildroot%_datadir/simutrans

%files
%_datadir/simutrans

%changelog
* Tue Mar 14 2023 Artyom Bystrov <arbars@altlinux.org> 123.0-alt1
- initial build for ALT Sisyphus

* Tue Jan 11 2022 Michiel van der Wulp <michiel.vanderwulp@gmail.com> - 123.0
- update to version 123.0 to match simutrans 123.0
* Thu Oct 22 2020 Michiel van der Wulp <michiel.vanderwulp@gmail.com>
- update to version 122.0 to match simutrans 122.0
* Thu Aug 27 2020 Matthias Mailänder <mailaender@opensuse.org>
- update to version 121.0 to match simutrans
* Tue Sep 25 2018 Michiel van der Wulp <michiel.vanderwulp@gmail.com>
- update to 120.4.1 for simutrans 120.4.1
- include the optional food chain
* Wed Sep 19 2018 Michiel van der Wulp <michiel.vanderwulp@gmail.com>
- update to 120.4 for simutrans 120.4
- include the optional food chain
* Sun Feb 18 2018 michiel.vanderwulp@gmail.com
- update to 120.3 for simutrans 120.x
- did not add the food pack (simupak64-addon-food-112-2)
* Tue Mar 21 2017 rpm@fthiessen.de
- Support https://en.opensuse.org/SourceUrls
- Fixed file duplicate warning (use fdupes)
- Fixed copyright
- did not add the food pack
* Tue Mar 21 2017 michiel.vanderwulp@gmail.com
- update to 120.2 for simutrans 120.x
- added the food pak to the same zip file
* Sat Jan  9 2016 michiel.vanderwulp@gmail.com
- update to 120.1.2 for simutrans 120.x
* Tue Mar 17 2015 michiel.vanderwulp@gmail.com
- update to 120.0.1 for simutrans 120.0
- the previously optional food chain has been incorporated in the main file
* Fri Feb 21 2014 michiel.vanderwulp@gmail.com
- update to 112.3 for simutrans 112.3
- this pak includes the optional food chain
* Thu Dec 27 2012 mailaender@opensuse.org
- initial package release (version 112.1)
