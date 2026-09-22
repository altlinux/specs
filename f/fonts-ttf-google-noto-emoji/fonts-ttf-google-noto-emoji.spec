%define _unpackaged_files_terminate_build 1

Name: fonts-ttf-google-noto-emoji
Version: 2.051
Release: alt1
Epoch: 1

Summary: Google "Noto Color Emoji" font
# The shipped NotoColorEmoji.ttf is under the SIL Open Font License; the
# upstream tooling carried in the source tarball is under Apache 2.0.
License: OFL-1.1 and Apache-2.0
Group: System/Fonts/True type
Url: https://github.com/googlefonts/noto-emoji
Vcs: https://github.com/googlefonts/noto-emoji.git
BuildArch: noarch

Source: %name-%version.tar
Source1: com.google.fonts.noto-color-emoji.metainfo.xml

BuildRequires(pre): rpm-build-fonts

# Was a separate -color subpackage until the black-and-white font was
# dropped upstream; fold it into the main package.
Obsoletes: fonts-ttf-google-noto-emoji-color < %EVR
Provides: fonts-ttf-google-noto-emoji-color = %EVR
Obsoletes: google-noto-color-emoji-fonts < 20150617
Provides: google-noto-color-emoji-fonts = 20150617

%description
This package provides the Google "Noto Color Emoji" font.

%prep
%setup

%install
# %%ttf_fonts_install takes every *.ttf in the current directory and upstream
# ships eight variants of the font, so stage the one that is packaged.
mkdir -p noto-color-emoji
cp -al fonts/NotoColorEmoji.ttf noto-color-emoji/
cd noto-color-emoji
%ttf_fonts_install google-noto-emoji
cd ..

install -m 0755 -d %buildroot%_datadir/metainfo
install -m 0644 -p %{SOURCE1} %buildroot%_datadir/metainfo/

%files -f noto-color-emoji/google-noto-emoji.files
%doc --no-dereference LICENSE
%doc AUTHORS CONTRIBUTING.md CONTRIBUTORS README.md
%_datadir/metainfo/com.google.fonts.noto-color-emoji.metainfo.xml

%changelog
* Tue Sep 22 2026 Ajrat Makhmutov <rauty@altlinux.org> 1:2.051-alt1
- New version.
- Drop the black-and-white NotoEmoji font, removed by upstream.
- Fold the former -color subpackage into the main package.
- Pack the source from the upstream git tag.
- Install the font per the ALT fonts policy: it now lives in
  /usr/share/fonts/ttf/google-noto-emoji, with an X11 catalogue entry.
- Rewrite the AppStream metainfo, which appstreamcli rejected as invalid.
- Spec cleanup.

* Sat May 25 2024 Ajrat Makhmutov <rauty@altlinux.org> 1:2.042-alt1
- new version (closes: 49013)

* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 20210716-alt1_2
- new version

* Fri Oct 01 2021 Igor Vlasenko <viy@altlinux.org> 20210716-alt1_1
- update to new release by fcimport

* Mon Jan 25 2021 Igor Vlasenko <viy@altlinux.ru> 20200916-alt1_1
- update to new release by fcimport

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 20200723-alt1_2
- update to new release by fcimport

* Wed Feb 26 2020 Igor Vlasenko <viy@altlinux.ru> 20191019-alt1_2
- update to new release by fcimport

* Wed Sep 18 2019 Igor Vlasenko <viy@altlinux.ru> 20190829-alt1_1
- update to new release by fcimport

* Wed Aug 07 2019 Igor Vlasenko <viy@altlinux.ru> 20190709-alt1_2
- update to new release by fcimport

* Thu Jun 20 2019 Igor Vlasenko <viy@altlinux.ru> 20180814-alt1_2
- new version

