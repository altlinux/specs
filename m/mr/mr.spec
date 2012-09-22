Name: mr
Version: 1.13
Release: alt1
Summary: A multiple repository management tool

Group: Development/Tools
License: GPLv2+
Url: http://kitenet.net/~joey/code/mr/
Source0: %name-%version.tar
Patch0: %name-%version-alt.patch
BuildArch: noarch

BuildRequires: perl-podlators

%description
The mr command can checkout, update, or perform other actions on
a set of repositories as if they were one combined respository. It
supports any combination of subversion, git, cvs, mecurial, bzr and
darcs repositories, and support for other revision control systems
can easily be added.

%prep
%setup
%patch0 -p1 -b .alt

%build
make %{?_smp_mflags}

%install
install -Dp -m 0755 %name %buildroot%_bindir/%name
for file in mr.1 webcheckout.1; do
    install -Dp -m 0644 $file %buildroot%_mandir/man1/$file
done
for file in lib/git-fake-bare lib/git-svn lib/unison; do
    install -Dp -m 0644 $file %buildroot%_datadir/%name/$file
done

%files
%_bindir/%name
%_datadir/%name/
%_man1dir/*.1.*
%doc GPL README TODO mrconfig mrconfig.complex

%changelog
* Sat Sep 22 2012 Terechkov Evgenii <evg@altlinux.org> 1.13-alt1
- 1.13

* Sat Sep 22 2012 Terechkov Evgenii <evg@altlinux.org> 1.12-alt1
- Initial build for ALT Linux Sisyphus (based on Fedora spec)
