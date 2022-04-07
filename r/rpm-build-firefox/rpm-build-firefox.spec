Summary: RPM helper macros to rebuild firefox packages

Name:    rpm-build-firefox
Version: 99.0
Release: alt3
License: MPL-2.0
Group:   Development/Other

Packager: Alexey Gladkov <legion@altlinux.ru>

BuildArch: noarch

Requires: mozilla-common-devel

%description
These helper macros provide possibility to rebuild
firefox packages by some Alt Linux Team Policy compatible way.

%install
mkdir -p -- %buildroot/%_rpmmacrosdir

cat > %buildroot/%_rpmmacrosdir/firefox <<EOF
%%firefox_cid   \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%%firefox_name  firefox

%%firefox_prefix  %%_libdir/%%firefox_name
%%firefox_datadir %%_datadir/%%firefox_name

%%firefox_arch_extensionsdir   %%mozilla_arch_extdir/%%firefox_cid
%%firefox_noarch_extensionsdir %%mozilla_noarch_extdir/%%firefox_cid
EOF

%files
%_rpmmacrosdir/firefox

%changelog
* Thu Apr 07 2022 Alexey Gladkov <legion@altlinux.ru> 99.0-alt3
- Rebuilt to get back into the repository.

* Tue Jul 13 2021 Alexey Gladkov <legion@altlinux.ru> 90.0-alt1
- Move rpm-build-firefox from firefox to separate package.

