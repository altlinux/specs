BuildRequires(pre): rpm-build-python

Name: screenkey
Version: 0.3
Release: alt1
Summary: A screen-cast tool to show your keys and based on key-mon project

Group: Video
License: GPL+
Url: https://launchpad.net/screenkey
Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar

BuildRequires: python-base python-devel python-modules python-modules-compiler python-modules-email

%description
A screen-cast tool to show your keys inspired by Screenflick and based on
the key-mon project.

%prep
%setup
sed -i 's/^Categories=.*/Categories=AudioVideo;Video;Recorder;/' data/screenkey.desktop
sed -i '/^Version=/d' data/screenkey.desktop

%build
%python_build

%install
mkdir -p %buildroot%_docdir/%name-%version
find build/lib* -name '*.py' -exec sed -i "1{/^#!/d}" {} \; && \
%python_install

%files
%doc
%_bindir/screenkey
%_desktopdir/screenkey.desktop
%python_sitelibdir_noarch/Screenkey
%exclude %python_sitelibdir_noarch/*.egg-info

%changelog
* Thu Sep 05 2013 Denis Smirnov <mithraen@altlinux.ru> 0.3-alt1
- %name.desktop fixes

* Wed Sep 04 2013 Denis Smirnov <mithraen@altlinux.ru> 0.2-alt1
- initial build for ALT Linux Sisyphus
