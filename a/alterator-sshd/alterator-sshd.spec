%define _altdata_dir %_datadir/alterator

Name: alterator-sshd
Version: 0.3
Release: alt1

Packager:  Dmitriy Kruglikov <dkr@altlinux.ru>

BuildArch: noarch

Source:%name-%version.tar.gz

Summary: OpenSSHd system configuration module
License: GPL
Group: System/Configuration/Other
Requires: alterator >= 4.8-alt1
Requires: alterator-fbi >= 5.11-alt2
Requires: alterator-l10n >= 2.9-alt8
Requires: alterator-service-functions >= 1.0
Conflicts: alterator >= 5.0
Conflicts: alterator-fbi >= 6.0
Conflicts: alterator-service-functions >= 2.0

# Automatically added by buildreq on Wed Apr 08 2009
BuildRequires: alterator rpm-macros-fillup

%description
OpenSSHd system configuration module

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_alterator_datadir/applications/*
%_alterator_datadir/ui/sshd
%_alterator_backend3dir/sshd


%changelog
* Wed Jul 07 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.3-alt1
- RC Candidate

* Wed Jul 07 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.2-alt3
- test release

* Fri Jul 02 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.2-alt2
- test release

* Fri Jun 25 2010 Dmitriy Kruglikov <dkr@altlinux.ru> 0.1-alt1
- Initial release.
