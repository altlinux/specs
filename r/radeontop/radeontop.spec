Name: radeontop
Version: 1.4
Release: alt2

Summary: Console utility for monitoring Radeon graphics cards
Summary(ru_RU.UTF-8): Консольная утилита для мониторинга видеокарт Radeon
License: GPL-3.0-only
Group: System/Kernel and hardware
Url: https://github.com/clbr/%name

# Source-url: https://github.com/clbr/radeontop/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Patch: %name-1.4-alt-makefile.patch

BuildRequires: gettext
BuildRequires: libdrm-devel
BuildRequires: libncursesw-devel
BuildRequires: libpciaccess-devel
BuildRequires: libxcb-devel
BuildRequires: libappstream-glib

%description
View Radeon GPU utilization, both for the total activity percent and
individual blocks. Supports R600 and up. Works with both the open drivers and
AMD Catalyst. For the Catalyst driver, only the mem path is currently
supported - this means it won't run on kernels that block /dev/mem.
Requires root access to /dev/mem or /dev/dri/card#

%description -l ru_RU.UTF-8
Просмотр загрузки графического процессора Radeon как для общего процента
активности, так и для отдельных блоков. Поддерживает R600 и выше. Работает как
с открытыми драйверами, так и с AMD Catalyst. Для драйвера Catalyst в
настоящее время поддерживается только путь mem - это означает, что он не будет
работать на ядрах, которые блокируют /dev/mem.
Требуется root-доступ к /dev/mem или /dev/dri/card#

%prep
%setup
patch -p1
sed -i 's/unknown/%version/' getver.sh

%build
%add_optflags
%make_build amdgpu=1 xcb=1 CC="gcc -g"

%install
mkdir -p %buildroot%_datadir/metainfo
install -Dm 0644 -p %name.metainfo.xml %buildroot%_datadir/metainfo/
%makeinstall_std LIBDIR=%_lib

%find_lang %name

%files -f %name.lang
%doc README.md COPYING
%_bindir/%name
%_man1dir/%name.1*
%_datadir/metainfo/%name.metainfo.xml
# Workaround failure to build on /usr/lib64
%_libdir/libradeontop_xcb.so

%changelog
* Tue May 31 2022 Evgeny Chuck <koi@altlinux.org> 1.4-alt2
- correct license information
- cleanup spec

* Tue May 31 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.4-alt1
- new version

* Mon May 30 2022 Vadim Illarionov <gbIMoBou@gmail.com> 1.4-alt0
- Initial build.
