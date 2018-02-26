Name: rpmrebuild
Version: 2.7
Release: alt2
License: GPLv2+
Group: Development/Other
Summary: A tool to build rpm file from rpm database
Source: %name-%version.tar.gz
Url: http://rpmrebuild.sourceforge.net/
BuildArch: noarch

Requires: /usr/bin/rpmbuild
# due to rpmrebuild.sh
Requires: setarch

%description
Rpmrebuild is a tool to build an RPM file from a package that has
already been installed in a basic use, rpmrebuild use do not require any
rpm building knowledge (On debian, the equivalent product is
dpkg-repack)

%package un_prelink
Group: Development/Other
Summary: An prelink -u plugin for %name
Requires: %name = %version-%release

%description un_prelink
Rpmrebuild plugin for automatically un-prelinking package content.

%prep
%setup -c %name-%version

%build
%make

%install
%makeinstall_std

%find_lang --with-man --output %name.lang ".*"

%files -f %name.lang
%doc Changelog News README Release Todo VERSION Version
%exclude %_man1dir/un_prelink.plug*
%exclude %_mandir/*/*/un_prelink.plug*
%exclude %prefix/lib/%name/plugins/un_prelink*

%_bindir/*
%dir %prefix/lib/%name
%prefix/lib/%name/*

%files un_prelink
%_man1dir/un_prelink.plug*
%_mandir/*/*/un_prelink.plug*
%prefix/lib/%name/plugins/un_prelink*

%changelog
* Tue Jun 19 2012 Dmitry V. Levin <ldv@altlinux.org> 2.7-alt2
- Fixed package requirements.

* Mon Jun 18 2012 Fr. Br. George <george@altlinux.ru> 2.7-alt1
- Autobuild version bump to 2.7
- Separate package requiring prelink

* Tue Aug 16 2011 Fr. Br. George <george@altlinux.ru> 2.6-alt1
- Autobuild version bump to 2.6

* Sat Apr 16 2011 Fr. Br. George <george@altlinux.ru> 2.4-alt1
- Initial build from scratch

