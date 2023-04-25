%define angie_pro_repos https://download.angie.software/angie-pro/altlinux
%define angie_keyid 617AB978CB849A76
%define _unpackaged_files_terminate_build 1

%ifdef _priority_distbranch
%define altbranch %_priority_distbranch
%else
%define altbranch %(rpm --eval %%_priority_distbranch)
%endif
%if "%altbranch" == "%nil"
%define altbranch sisyphus
%endif

Name: angie-pro-repo
Version: 1.0.4
Release: alt1

Summary: Link to the Angie PRO repository and GPG-key
License: GPL-3
Group: System/Configuration/Packaging

BuildArch: noarch

Source: %name-%version.tar
Url: https://wbsrv.ru/angie-pro/docs/install/

Packager: Leonid Krivoshein <klark@altlinux.org>

Requires: apt-conf
Requires: apt-https
Requires: alt-gpgkeys

%description
Angie is an efficient, powerful and scalable web server, that was
forked from nginx by some of its former core devs, with intention
to extend functionality far beyond original version.

Angie is a drop-in replacement for nginx, so you can use existing
nginx configuration without major changes.

This package contains just a link to the Angie PRO repository and
GPG key.

%prep
%setup

%build
%if "%altbranch" == "p10"
echo "rpm [angie] %angie_pro_repos/10/ %_arch main" \
	> etc/apt/sources.list.d/angie-pro.list
chmod 0644 etc/apt/sources.list.d/angie-pro.list
%endif
sed -i 's/@angie_keyid@/%angie_keyid/' \
	usr/lib/rpm/angie-repo.filetrigger
mkdir -p -m0755 %buildroot
mv -f etc usr %buildroot/

%post
echo "/usr/lib/alt-gpgkeys/pubring.gpg" |
	/usr/lib/rpm/angie-repo.filetrigger

%files
%dir /etc/ssl/angie
/etc/ssl/angie/angie-signing.gpg
/etc/apt/vendors.list.d/angie.list
%config(noreplace) /etc/apt/apt.conf.d/angie-pro.conf
%config(noreplace) /etc/apt/sources.list.d/angie-pro.list
%ghost %config(noreplace) /etc/ssl/angie/angie-repo.key
%ghost %config(noreplace) /etc/ssl/angie/angie-repo.crt
/usr/lib/rpm/angie-repo.filetrigger

%changelog
* Tue Apr 25 2023 Leonid Krivoshein <klark@altlinux.org> 1.0.4-alt1
- Added virtual dependency on apt-conf.

* Mon Apr 24 2023 Leonid Krivoshein <klark@altlinux.org> 1.0.3-alt1
- Dropped explicit dependency on apt-conf-branch (ALT #45938).

* Thu Apr 20 2023 Leonid Krivoshein <klark@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus.

