%define py_name yt_dlp

Name: yt-dlp
Version: 2023.03.04
Release: alt1

Summary: A tool for downloading from video services for offline watching
License: Unlicense
Group: Networking/File transfer
Url: https://github.com/yt-dlp/yt-dlp

Source0: %name-%version.tar

BuildArch: noarch

Requires: python3-module-%py_name = %EVR

# Automatically added by buildreq on Tue Mar 07 2023
# optimized out: libgpg-error python3 python3-base python3-dev python3-module-pkg_resources python3-module-setuptools sh4
BuildRequires: python3-module-pyproject-installer python3-module-wheel

BuildRequires(pre): rpm-build-python3

%description
yt-dlp is a small command-line program to retrieve videos from
YouTube.com and other video hosting services for offline watching.

A youtube-dl fork with additional features and fixes.

%package -n python3-module-%py_name
Group: Development/Python
Summary: Python 3 module for yt-dlp

%description -n python3-module-%py_name
yt-dlp is a small command-line program to retrieve videos from
YouTube.com and other video hosting services for offline watching.

A youtube-dl fork with additional features and fixes.

This package contains Python 3 module.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

rm %buildroot/usr/share/doc/yt_dlp/README.txt
rm -r %buildroot%python3_sitelibdir/%py_name/__pyinstaller

%define _unpackaged_files_terminate_build 1

%files
%_bindir/yt-dlp
%_man1dir/yt-dlp.1.*
%doc README.txt

%_datadir/bash-completion/completions/yt-dlp
%_datadir/fish/vendor_completions.d/yt-dlp.fish
%_datadir/zsh/site-functions/_yt-dlp

%files -n python3-module-%py_name
%python3_sitelibdir/%py_name
%python3_sitelibdir/%py_name-*.dist-info

%changelog
* Tue Mar 07 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 2023.03.04-alt1
- Updated to 2023.03.04.
- python3-module-%py_name: dropped __pyinstaller hook to get rid
  of PyInstaller requirement.
- spec: switched to modern %%pyproject_* macros.

* Sat Feb 18 2023 Cronbuild Service <cronbuild@altlinux.org> 2023.02.17-alt1
- Updated to 2023.02.17.

* Mon Jan 09 2023 Cronbuild Service <cronbuild@altlinux.org> 2023.01.06-alt1
- Updated to 2023.01.06.

* Fri Jan 06 2023 Cronbuild Service <cronbuild@altlinux.org> 2023.01.02-alt1
- Updated to 2023.01.02.

* Mon Nov 14 2022 Cronbuild Service <cronbuild@altlinux.org> 2022.11.11-alt1
- Updated to 2022.11.11.

* Thu Oct 06 2022 Cronbuild Service <cronbuild@altlinux.org> 2022.10.04-alt1
- Updated to 2022.10.04.

* Sun Sep 04 2022 Cronbuild Service <cronbuild@altlinux.org> 2022.09.01-alt1
- Updated to 2022.09.01.

* Fri Aug 19 2022 Cronbuild Service <cronbuild@altlinux.org> 2022.08.19-alt1
- Updated to 2022.08.19.

* Tue Aug 09 2022 Cronbuild Service <cronbuild@altlinux.org> 2022.08.08-alt1
- Updated to 2022.08.08.

* Wed Jul 20 2022 Cronbuild Service <cronbuild@altlinux.org> 2022.07.18-alt1
- Updated to 2022.07.18.

* Thu Jun 30 2022 Cronbuild Service <cronbuild@altlinux.org> 2022.06.29-alt1
- Updated to 2022.06.29.

* Wed Jun 22 2022 Cronbuild Service <cronbuild@altlinux.org> 2022.06.22.1-alt1
- Updated to 2022.06.22.1.

* Sat May 21 2022 Cronbuild Service <cronbuild@altlinux.org> 2022.05.18-alt1
- Updated to 2022.05.18.

* Mon Apr 11 2022 Cronbuild Service <cronbuild@altlinux.org> 2022.04.08-alt1
- Updated to 2022.04.08.

* Wed Mar 09 2022 Cronbuild Service <cronbuild@altlinux.org> 2022.03.08.1-alt1
- Updated to 2022.03.08.1.

* Sun Feb 06 2022 Cronbuild Service <cronbuild@altlinux.org> 2022.02.04-alt1
- Updated to 2022.02.04.

* Sun Jan 23 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 2022.01.21-alt1
- Updated to 2022.01.21.

* Sun Jan 09 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 2021.12.27-alt1
- Initial build for ALT Sisyphus (2021.12.27) (ALT#41434).
