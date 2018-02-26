Name: appliance-ve-std
Summary: Virtual package for most VEs
BuildArch: noarch
Version: 4.0.1
Release: alt1
License: GPL
Group: System/Base

Requires: appliance-base-sshd
Requires: appliance-ve-minimal
Requires: su
Requires: syskeeper-ve

# Admins wants to work in nice enviroment :)
Requires: vim-enhanced
Requires: mc
Requires: zsh

# Useful for see git-repos created by etckeeper and syskeeper
Requires: tig

# Every server (virtual or not) required to have MTA
# More lightweight replacments has some critical problems
Requires: postfix

%description
%summary

%files

%changelog
* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

