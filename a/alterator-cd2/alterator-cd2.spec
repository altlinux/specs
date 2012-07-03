%define distro_version 5.0

%define _altdata_dir %_datadir/alterator

Name: alterator-cd2
Version: 0.3
Release: alt3

%add_findreq_skiplist %_datadir/install2/preinstall.d/*

Packager: Stanislav Ievlev <inger@altlinux.org>

BuildArch: noarch

Source:%name-%version.tar

Summary: additional cdrom installation
License: GPL
Group: System/Configuration/Other

Requires: alterator >= 4.10-alt7
Requires: alterator-l10n >= 2.4-alt11
Requires: alterator-pkg

BuildPreReq: alterator >= 4.10-alt7

%description
installer's step for an additional cdrom installation

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_datadir/install2/preinstall.d/*
%_datadir/alterator/ui/*
%_alterator_backend3dir/*

%changelog
* Tue Aug 18 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt3
- 10-cd2.sh fixed for network install

* Thu Aug 06 2009 Stanislav Ievlev <inger@altlinux.org> 0.3-alt2
- remove debug message

* Thu Aug 06 2009 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- add i18n support

* Wed Aug 05 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- preinstall script added

* Wed Aug 05 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
