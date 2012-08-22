Name: gkrellm-themes
Version: 1.0
Release: alt1.qa1

Summary: Gkrellm themes
Summary(ru_RU.UTF-8): Темы для gkrellm
License: GPL
Group: Monitoring
Url: http://www.muhri.net/gkrellm/
Buildarch: noarch

Source0: http://www.muhri.net/gkrellm/GKrellM-Skins.tar.bz2

Requires: gkrellm >= 2.2.0

Summary(ru_RU.UTF-8): Темы для gkrellm

%description
Gkrellm themes

%description -l ru_RU.UTF-8
Темы для gkrellm

%prep
%setup -q -n GKrellM-skins

%build

%install
mkdir -p %buildroot%_datadir/gkrellm2/themes
for i in *.tar.gz; do tar xzv -C %buildroot%_datadir/gkrellm2/themes -f $i; done

# broken symlinks in version 1.0
#find-provides: broken symbolic link /var/tmp/gkrellm-themes-buildroot/usr/share/gkrellm2/themes/twilite/.png -> green/frame_right-green.png is not going to provide anything
ln -sf green/frame_right.png %buildroot%_datadir/gkrellm2/themes/twilite/.png

# It is the file in the package whose name matches the format emacs or vim uses 
# for backup and autosave files. It may have been installed by  accident.
find $RPM_BUILD_ROOT \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete
# failsafe cleanup if the file is declared as %%doc
find . \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete

%files
%_datadir/gkrellm2/themes

%changelog
* Wed Aug 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * backup-file-in-package for gkrellm-themes
  * utf8 experimental recoder

* Mon Jan 10 2005 Serge Pavlovsky <pal@altlinux.ru> 1.0-alt1
- built for Sisyphus

