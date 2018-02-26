Name:		rpm-build-suse-compat
Version:	0.01
Release:	alt1
Summary:	Compatibility environment to build SuSE rpms
License:	GPL2+
Group:		Development/Other

Source:		%name-%version.tar
Patch:		update-desktop-files-alt-%version.patch
BuildArch:	noarch
Requires:	rpm-macros-suse-compat = %version-%release

%description
%summary

%package -n	rpm-macros-suse-compat
Group:		Development/Other
Summary:	SuSE compatibility macros

%description -n rpm-macros-suse-compat
%summary

%prep
%setup -q

%build

%install
mkdir -p %buildroot%_rpmlibdir
install -m0755 update-desktop-files/suse_update_desktop_file.sh update-desktop-files/map-desktop-category.sh %buildroot%_rpmlibdir/

install -m0644 -D update-desktop-files/macro %buildroot%_rpmmacrosdir/suse-compat

%files
%_rpmlibdir/*.sh

%files -n rpm-macros-suse-compat
%_rpmmacrosdir/suse-compat

%changelog
* Mon Jan 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- build for Sisyphus

