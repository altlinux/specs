Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-emacs
BuildRequires: /usr/bin/pod2man rpm-build-python3
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global spectool_version 1.0.10

Name:           rpmdevtools
Version:        9.6
Release:        alt2
Summary:        RPM Development Tools

# rpmdev-setuptree is GPLv2, everything else GPLv2+
License:        GPLv2+ and GPLv2
URL:            https://pagure.io/rpmdevtools
# Sources:      https://releases.pagure.org/rpmdevtools/%{name}-%{version}.tar.xz
Source:         %name-%version.tar

# Backports from upstream
Patch:          %name-%version-alt.patch

BuildArch:      noarch
# help2man, pod2man, *python for creating man pages
BuildRequires:  help2man
BuildRequires:  %{_bindir}/pod2man
BuildRequires:  rpm-build-perl
BuildRequires:  python3
BuildRequires:  python3-module-rpm
BuildRequires:  bash-completion
# rpmdev-spectool
BuildRequires:  python3(progressbar)
BuildRequires:  python3(requests)
BuildRequires:  python3(rpm)
Provides:       spectool = %{spectool_version}
Requires:       curl
Requires:       diffutils
Requires:       fakeroot
Requires:       file
Requires:       findutils
Requires:       gawk
Requires:       grep
Requires:       python3-module-rpm
Requires:       sed
#Requires:       emacs-filesystem

###########################
# removed/split components:
Requires: spectool
Requires: qa-robot
Requires: rpmpeek
%add_findreq_skiplist /usr/share/rpmdevtools/*
%add_findreq_skiplist /etc/rpmdevtools/template.init
%add_findreq_skiplist %_bindir/rpmdev-extract
Packager: Igor Vlasenko <viy@altlinux.org>
###########################


%description
This package contains scripts and (X)Emacs support files to aid in
development of RPM packages.
rpmdev-setuptree    Create RPM build tree within user's home directory
rpmdev-diff         Diff contents of two archives
rpmdev-newspec      Creates new .spec from template
rpmdev-rmdevelrpms  Find (and optionally remove) "development" RPMs
rpmdev-checksig     Check package signatures using alternate RPM keyring
rpminfo             Print information about executables and libraries
rpmdev-md5/sha*     Display checksums of all files in an archive file
rpmdev-vercmp       RPM version comparison checker
rpmdev-wipetree     Erase all files within dirs created by rpmdev-setuptree
rpmdev-extract      Extract various archives, "tar xvf" style
rpmdev-bumpspec     Bump revision in specfile
...and many more.


%prep
%setup -q
%patch -p1

grep -lF "%{_bindir}/python " * \
| xargs sed -i -e "s|%{_bindir}/python |%{_bindir}/python3 |"


%build
%autoreconf
%configure --libdir=%{_prefix}/lib
%make_build


%install

%makeinstall_std

echo %%{_datadir}/bash-completion > %{name}.files
[ -d $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d ] && \
echo %%{_sysconfdir}/bash_completion.d > %{name}.files

#for dir in %{_emacs_sitestart_dir} ; do
#  install -dm 755 $RPM_BUILD_ROOT$dir
#  ln -s %{_datadir}/rpmdevtools/rpmdev-init.el $RPM_BUILD_ROOT$dir
#  touch $RPM_BUILD_ROOT$dir/rpmdev-init.elc
#done
#for rpm404_ghost in %{_emacs_sitestart_dir}/rpmdev-init.elc
#do
#    mkdir -p %buildroot`dirname "$rpm404_ghost"`
#    touch %buildroot"$rpm404_ghost"
#done

pushd %buildroot%_man1dir
rm -f spectool* rpmpeek* rpmargs* rpmelfsym* rpmfile* rpmsodiff* rpmsoname*
popd
pushd %buildroot%_bindir
rm -f spectool rpmpeek rpmargs rpmelfsym rpmfile rpmsodiff rpmsoname
popd

%files -f %{name}.files
%doc --no-dereference COPYING
%doc NEWS
%config(noreplace) %{_sysconfdir}/rpmdevtools/
%{_datadir}/rpmdevtools/
%{_bindir}/rpm*
#%{_emacs_sitestart_dir}/rpmdev-init.el
#%ghost %{_emacs_sitestart_dir}/rpmdev-init.elc
%{_mandir}/man[18]/*.[18]*


%changelog
* Mon Sep 05 2022 Evgeny Sinelnikov <sin@altlinux.org> 9.6-alt2
- Add support of ALT releases in rpmdev-bumpspec
- Adopt for ALT first spectemplates: dummy, lib and minimal
- Adopt rpmdev-newspec support for ALT specific rpm

* Mon Sep 05 2022 Evgeny Sinelnikov <sin@altlinux.org> 9.6-alt1
- Update to latest release

* Mon May 17 2021 Igor Vlasenko <viy@altlinux.org> 8.10-alt2
- fixed build

* Tue Jan 14 2020 Igor Vlasenko <viy@altlinux.ru> 8.10-alt1
- new version

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 6.4-alt1.1.1.1
- Rebuild with Python-2.7

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.4-alt1.1.1
- Rebuilt with python 2.6

* Sun Feb 10 2008 Grigory Batalov <bga@altlinux.ru> 6.4-alt1.1
- Rebuilt with python-2.5.

* Wed Dec 05 2007 Igor Vlasenko <viy@altlinux.ru> 6.4-alt1
- first build for ALT Linux;
- removed included at@' qa-robot :)
- spectool is built in a separate source;
- added dependency on qa-robot and spectool.
- TODO: emacs and xemacs.

