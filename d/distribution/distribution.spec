Name: distribution
Version: 1.2.2
Release: alt2

Summary: Short, simple, direct scripts for creating character-based graphs
License: GPLv2
Group: Text tools
URL: https://github.com/philovivero/distribution
BuildArch: noarch

Source0: %name-%version.tar


%description
Short, simple, direct scripts for creating character-based graphs in a
command terminal. Status: stable. Features added very rarely.

%package perl
Summary: %summary
Group: Text tools
Requires: %name = %version-%release

%description perl
%summary

This is perl implementation

%package python
Summary: %summary
Group: Text tools
Requires: %name = %version-%release

%description python
%summary

This is python implementation

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%install
mkdir -p %buildroot%_bindir
for file in %name %name.py;do
install -p -m755 $file %buildroot%_bindir/
done

%files perl
%_bindir/%name

%files python
%_bindir/%name.py

%files
%doc README.md VERSION screenshot.png distributionrc


%changelog
* Wed Oct 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.2.2-alt2
- python2 -> python3

* Fri Jan  8 2016 Terechkov Evgenii <evg@altlinux.org> 1.2.2-alt1
- Initial build for ALT Linux Sisyphus
