# SPEC file for gilolite package

Name: gitolite
Version: 3.6.13
Release: alt1

Summary: Highly flexible server for git directory version tracker
License: %gpl2only
Group: System/Servers

Url: https://gitolite.com/gitolite/
#Url: http://github.com/sitaramc/gitolite
Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

# Patched qt version is able to function without X-server running
# https://github.com/wkhtmltopdf/qt
Source1: doc-%version.tar
Patch1:  doc-%version-%release.patch


Source2: README.ALT
Source3: gitolite.logrotate

# (fedora) Far from being upstreamable
Patch2: gitolite-3.0-rpm.patch

Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

# Automatically added by buildreq on Fri Jul 16 2021 (-bi)
# optimized out: bash4 bashrc cmake-modules gem-bundler gem-method-source gem-power-assert gem-rake gem-setup git-core libsasl2-3 openssh-common perl perl-IO-Socket-Timeout perl-PerlIO-via-Timeout perl-Try-Tiny perl-parent python3 python3-base python3-module-paste rpm-build-python3 ruby ruby-coderay ruby-rdoc ruby-stdlibs setup-rb sh4
BuildRequires: perl-Encode perl-Text-Balanced perl-Redis

BuildRequires(pre): rpm-build-licenses
BuildRequires: perl-Text-Markdown

# Redis cache module tries to start Redis server - we obviously don't want this inside BTE
%add_findreq_skiplist */Gitolite/Cache.pm

%define gitolite_homedir %_localstatedir/%name

%description
Gitolite allows a server to host many git repositories and
provide access to many developers, without having to give them
real userids on the server.  The essential magic in doing this
is ssh's pubkey access and the authorized keys file, and the
inspiration was an older program called gitosis.

Gitolite can restrict who can read from (clone/fetch) or write
to (push) a repository. It can also restrict who can push to what
branch or tag, which is very important in a corporate environment.
Gitolite can be installed without requiring root permissions, and
with no additional software than git itself and perl. It also has
several other neat features described below and elsewhere in the
doc/ directory.

%package doc
Summary: documentation for the gitolite server
Group: Documentation

%description doc
Gitolite allows a server to host many git repositories and
provide access to many developers, without having to give them
real userids on the server.

This package contains Gitolite documentation.


%prep
%setup
%patch0 -p1

mkdir doc
pushd doc
tar -x -f %SOURCE1
patch -p1 < %PATCH1
popd


%patch2
cp %SOURCE2 .

mv -f -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
# Contributed test suite
rm -rf -- contrib/t

# Format documentation
find doc/docs/ -name '*.mkd' | while read F; do
    perl -MText::Markdown >${F/.mkd/.html} <$F \
        -e 'print Text::Markdown::markdown (join "", <>)'
done


%install
install -d %buildroot%gitolite_homedir/.ssh
install -d %buildroot%_bindir
install -d %buildroot%perl_vendor_privlib
install -d %buildroot%_datadir/%name
install -d %buildroot%_logdir/%name

install -p src/gitolite %buildroot%_bindir
install -p src/gitolite-shell %buildroot%_bindir
cp -a src/lib/* %buildroot%perl_vendor_privlib
cp -a src/{VREF,commands,syntactic-sugar,triggers} %buildroot%_datadir/%name
cp -a check-g2-compat convert-gitosis-conf %buildroot%_datadir/%name

touch %buildroot%gitolite_homedir/.ssh/authorized_keys

# VERSION file
echo "v%version-%release" > %buildroot%_datadir/%name/VERSION

install -d %buildroot%_logrotatedir
install -m 640 %SOURCE3 %buildroot%_logrotatedir/%name

## Documentation
mkdir -p docs/contrib
pushd doc/docs
cp    *.html ../../docs/
cp    contrib/*.html ../../docs/contrib
cp -a css/ ../../docs/
popd


%pre
# FIXME: _%name?
getent group %name >/dev/null || groupadd -r %name ||:
getent passwd %name >/dev/null || \
useradd -r -g %name -d %gitolite_homedir -s /bin/sh \
        -c "git repository hosting" %name ||:

%triggerpostun  -- gitolite < 3.0
echo "---------------- gitolite -------------------------"
echo "  WARNING: there are no automatic upgrade procedure"
echo "  from gitolite g2 (2.x) to the g3 (3.x)"
echo "  See instructions for manual migration in"
echo "  g2migr*.html files in doc directory."
echo "---------------------------------------------------"

%files
%doc README.markdown CHANGELOG CONTRIBUTING
%doc README.ALT
%doc --no-dereference COPYING
%doc contrib

%_bindir/*
%perl_vendor_privlib/*
%_datadir/%name

%attr(750,%name,%name) %dir %gitolite_homedir
%attr(750,%name,%name) %dir %gitolite_homedir/.ssh
%config(noreplace) %attr(640,%name,%name) %gitolite_homedir/.ssh/authorized_keys

%attr(0730,root,%name) %dir %_logdir/%name

%config %_logrotatedir/%name

%files doc
%doc docs/*


%changelog
* Mon Sep 11 2023 Nikolay A. Fetisov <naf@altlinux.org> 3.6.13-alt1
- New version

* Thu Feb 10 2022 Nikolay A. Fetisov <naf@altlinux.org> 3.6.12-alt2
- fix build process

* Fri Jul 16 2021 Nikolay A. Fetisov <naf@altlinux.org> 3.6.12-alt1
- restored from orphaned
- new version
- move documentation to the -doc subpackage

* Wed Jun 13 2012 Nikolay A. Fetisov <naf@altlinux.ru> 3.03-alt1
- new version (Closes: #27442)

* Wed Apr 20 2011 Michael Shigorin <mike@altlinux.org> 2.0-alt1
- initial build for ALT Linux Sisyphus
  + based on 2.0-1 fedora package by Jon Ciesla <limb/jcomserv.net>
