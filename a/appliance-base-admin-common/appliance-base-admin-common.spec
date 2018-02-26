Name: appliance-base-admin-common
Summary: Virtual package that require utilites for admins
BuildArch: noarch
Version: 4.0.1
Release: alt1
License: GPL
Group: System/Base

# System
Requires: appliance-base-basesystem
Requires: appliance-base-compress-all

# Shells
Requires: zsh
# Yes, this needed by many admins
Requires: mc
# Docs
Requires: man-pages
Requires: man-pages-ru
# Editor
Requires: vim-enhanced
# Other
Requires: rsync
Requires: su
Requires: sudo
Requires: screen
Requires: lsof

# man requries less
#less
Requires: file

# Removed from Sisyphus
#csed

%description
%summary

%files

%changelog
* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

