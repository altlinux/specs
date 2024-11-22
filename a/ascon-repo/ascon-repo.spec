%define _unpackaged_files_terminate_build 1

%define alt_keyring /usr/lib/alt-gpgkeys/pubring.gpg
%define ascon_repos https://repo.ascon.ru/stable/alt
%define ascon_keyid 03B4C6426AC2DB03

%ifdef _priority_distbranch
%define altbranch %_priority_distbranch
%else
%define altbranch %(rpm --eval %%_priority_distbranch)
%endif
%if "%altbranch" == "%nil"
%define altbranch sisyphus
%endif

Name: ascon-repo
Version: 1.1
Release: alt1

Summary: ASCON GPG-key and link to the ASCON repository
License: GPL-3
Group: System/Configuration/Packaging

BuildArch: noarch

Source: %name-%version.tar
Url: https://ascon.ru/products/

Packager: Leonid Krivoshein <klark@altlinux.org>

Requires: apt-conf
Requires: apt-https
Requires: alt-gpgkeys

%description
This package contains just a link to the ASCON repository and public GPG-key.

%prep
%setup

%build
%if "%altbranch" == "p10"
( echo "rpm [ascon] %ascon_repos/p10 %_arch main"
  echo "rpm [ascon] %ascon_repos/p10 noarch main"
) > etc/apt/sources.list.d/ascon.list
chmod 0644 etc/apt/sources.list.d/ascon.list
%endif
sed -i \
    -e 's,@alt_keyring@,%alt_keyring,' \
    -e 's,@ascon_keyid@,%ascon_keyid,' \
	usr/lib/rpm/ascon-repo.filetrigger
mkdir -p -m0755 %buildroot
mv -f etc usr %buildroot/

%preun
if [ -s "%alt_keyring" ] &&
   gpg --list-packets "%alt_keyring" |grep -F -qs "keyid: %ascon_keyid"
then
	echo "Removing ASCON GPG key form the public keyring..." >&2
	gpg --keyring "%alt_keyring" --no-default-keyring \
		--batch --yes --delete-keys "%ascon_keyid"
fi

%post
echo "%alt_keyring" |/usr/lib/rpm/ascon-repo.filetrigger

%files
%dir /etc/ssl/ascon
/etc/ssl/ascon/ascon-signing.gpg
/etc/apt/vendors.list.d/ascon.list
%config(noreplace) /etc/apt/sources.list.d/ascon.list
/usr/lib/rpm/ascon-repo.filetrigger

%changelog
* Fri Nov 22 2024 Leonid Krivoshein <klark@altlinux.org> 1.1-alt1
- Remove GPG-key whith the package.
- Updated ASCON GPG-key and spec.

* Sun Apr 28 2024 Leonid Krivoshein <klark@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.

