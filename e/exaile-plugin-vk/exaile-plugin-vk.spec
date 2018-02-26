%define plugin_path %_datadir/exaile/plugins/vk_exaile

Name: exaile-plugin-vk
Version: 0.0.3
Release: alt1.1
Summary: Listen to music from VKontakte
License: GPLv2
Group: Sound
Url: http://github.com/vrtx64/vk_exaile
Packager: Egor Glukhov <kaman@altlinux.org>
BuildArch: noarch
Source0: %name-%version.tar
Requires: exaile >= 0.3.2
Requires: wget

%add_python_req_skip xl
%add_python_req_skip xlgui


%description
vk_exaile is a plugin that plays music from vk.com.

%prep
%setup

%build

%install
mkdir -p %buildroot%plugin_path
for f in *.py preference.ui logo_vkontakte_bw.png
do
    install -m644 -p $f %buildroot%plugin_path
done

%files
%doc README
%plugin_path

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.3-alt1.1
- Rebuild with Python-2.7

* Wed Aug 25 2010 Egor Glukhov <kaman@altlinux.org> 0.0.3-alt1
- Initial build for Sisyphus

