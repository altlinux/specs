Name: magit
Version: 0.7
Release: alt5

Summary: A Emacs mode for Git
License: GPL3+
Group: Development/Other
Url: http://zagadka.vm.bytemark.co.uk/magit/
Source: %name-%version.tar
Patch: %name-%version-alt.patch

Packager: Evgenii Terechkov <evg@altlinux.org>

BuildRequires: emacs-nox
BuildPreReq: emacs-devel
BuildArch: noarch

%description
It's Magit! A Emacs mode for Git.

%prep
%setup
%patch -p1

%build
./autogen.sh
%configure
make
rm -rf %name.info
make info

%install
%makeinstall_std

%files
%_emacs_sitestart_dir/*
%_emacslispdir/%name.*
%_infodir/*.info*
%doc AUTHORS ChangeLog NEWS README

%changelog
* Sun Aug  1 2010 Terechkov Evgenii <evg@altlinux.ru> 0.7-alt5
- Upstream git-20100801

* Tue Apr 13 2010 Terechkov Evgenii <evg@altlinux.ru> 0.7-alt4
- Upstream git-20100413

* Sun Mar 21 2010 Terechkov Evgenii <evg@altlinux.ru> 0.7-alt3.4
- Upstream git-20100321

* Tue Mar 16 2010 Terechkov Evgenii <evg@altlinux.ru> 0.7-alt3.3
- Upstream git-20100316

* Sun Jan 10 2010 Terechkov Evgenii <evg@altlinux.ru> 0.7-alt3.2
- Patch to push in branches with different names

* Sat Jan  9 2010 Terechkov Evgenii <evg@altlinux.ru> 0.7-alt3.1
- Patch to customize magit-status buffer name format

* Sat Jan  9 2010 Terechkov Evgenii <evg@altlinux.ru> 0.7-alt3
- Upsream git-20100109
- 0001-Get-the-real-upstream-branch-instead-of-guessing-fro.patch rebased (seems actual)

* Sun Oct  4 2009 Terechkov Evgenii <evg@altlinux.ru> 0.7-alt2
- Apply "0001-Get-the-real-upstream-branch-instead-of-guessing-fro.patch (2)" (rediffed)
- Extrace alt-specific patch (branch alt-fixes)

* Fri Oct  2 2009 Terechkov Evgenii <evg@altlinux.ru> 0.7-alt1
- Initial build for ALT Linux Sisyphus
