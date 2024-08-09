%define py_name yt_dlp

Name: yt-dlp
Version: 2024.08.06
Release: alt1

Summary: A tool for downloading from video services for offline watching
License: Unlicense
Group: Networking/File transfer
Url: https://github.com/yt-dlp/yt-dlp

Source0: %name-%version.tar

BuildArch: noarch

Requires: python3-module-%py_name = %EVR

# The curl_cffi module is optional (but recommended) and
# is not currently packaged in ALT.
%add_python3_req_skip curl_cffi.const curl_cffi.requests

# Automatically added by buildreq on Tue Jun 18 2024
# optimized out: libgpg-error python3 python3-base python3-dev python3-module-packaging python3-module-pathspec python3-module-pluggy python3-module-trove-classifiers sh5
BuildRequires: python3-module-hatchling python3-module-pyproject-installer python3-module-setuptools

BuildRequires(pre): rpm-build-python3

# In the p10 branch, the python3-module-wheel package doesn't
# pull in setuptools.
BuildPreReq: python3-module-setuptools

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
* Fri Aug 09 2024 Cronbuild Service <cronbuild@altlinux.org> 2024.08.06-alt1
- Updated to 2024.08.06.

* Sun Aug 04 2024 Cronbuild Service <cronbuild@altlinux.org> 2024.08.01-alt1
- Updated to 2024.08.01.

* Fri Jul 26 2024 Cronbuild Service <cronbuild@altlinux.org> 2024.07.25-alt1
- Updated to 2024.07.25.

* Sun Jul 14 2024 Cronbuild Service <cronbuild@altlinux.org> 2024.07.09-alt1
- Updated to 2024.07.09.

* Sat Jul 06 2024 Cronbuild Service <cronbuild@altlinux.org> 2024.07.02-alt1
- Updated to 2024.07.02.

* Tue Jul 02 2024 Cronbuild Service <cronbuild@altlinux.org> 2024.07.01-alt1
- Updated to 2024.07.01.

* Tue Jun 18 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 2024.05.27-alt1
- Updated to 2024.05.27.

* Fri Jan 05 2024 Cronbuild Service <cronbuild@altlinux.org> 2023.12.30-alt1
- Updated to 2023.12.30.

* Tue Nov 21 2023 Cronbuild Service <cronbuild@altlinux.org> 2023.11.16-alt1
- Updated to 2023.11.16.

* Mon Oct 16 2023 Cronbuild Service <cronbuild@altlinux.org> 2023.10.13-alt1
- Updated to 2023.10.13.

* Mon Oct 09 2023 Cronbuild Service <cronbuild@altlinux.org> 2023.10.07-alt1
- Updated to 2023.10.07.

* Wed Sep 27 2023 Cronbuild Service <cronbuild@altlinux.org> 2023.09.24-alt1
- Updated to 2023.09.24.

* Sun Aug 20 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 2023.07.06-alt2
- Added GPG signature verification into the gear-cronbuild scripts.
- Added explicit BR: python3-module-setuptools to facilitate backports
  to p10 branch.

* Sun Jul 09 2023 Cronbuild Service <cronbuild@altlinux.org> 2023.07.06-alt1
- Updated to 2023.07.06.

* Fri Jun 23 2023 Cronbuild Service <cronbuild@altlinux.org> 2023.06.22-alt1
- Updated to 2023.06.22.

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
