Name: autorepo-altnode-admin-pkgset
Version: 0.01
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: admin tools for an automated packaging node
Group: Development/Other
License: ALT-Public-Domain
#Url:

# autorepo-altnode
Requires: autorepo-altnode-admin-scripts
# system tools
Requires: apt-scripts openssh

# user tools
Requires: hardlink hostinfo lsof mc strace su time tmux

%description
%summary

%prep

%build

%install

mkdir -p $RPM_BUILD_ROOT

%files

%changelog
* Mon Sep 12 2022 Igor Vlasenko <viy@altlinux.org> 0.01-alt1
- First build
