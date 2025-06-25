%global _unpackaged_files_terminate_build 1

Name: activitywatch-webui
Version: 1.0.0
Release: alt1
Summary: A web-based UI for ActivityWatch, built with Vue.js
License: MPL-2.0
Group: System/Servers
Url: https://activitywatch.net
VCS: https://github.com/ActivityWatch/aw-webui

Source: %name-%version.tar
Source1: node_modules.tar
Source2: external_media.tar
Patch: alt-fix-get-commit-hash.patch

# CPU time limit exceeded
ExcludeArch: i586

BuildRequires: npm

%description
Webapp for visualizing and browsing ActivityWatch data, built with Vue.js.

%prep
%setup -a 1 -a 2
%patch -p1

%build
export COMMIT_HASH=8add7f7b
npm run build

%install
mkdir -p %buildroot%_datadir/activitywatch-webui
cp -r dist/* media/logo/logo.png %buildroot%_datadir/activitywatch-webui

%files
%_datadir/activitywatch-webui
%doc LICENSE.txt

%changelog
* Tue Jun 10 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.0.0-alt1
- Initial build for ALT.
