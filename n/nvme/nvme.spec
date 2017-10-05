Name: nvme
Version: 1.4
Release: alt2
Summary: Core nvme tools
License: GPL
Group: System/Configuration/Hardware
Url: https://github.com/linux-nvme/nvme-cli/
Source: nvme-%version.tar
Provides: nvme
BuildRequires: libuuid-devel
Requires(post): util-linux

%description
NVMe is a fast, scalable, direct attached storage interface. The nvme
cli rpm installs core management tools with minimal dependencies.

%prep
%setup

%build
CFLAGS=%optflags \
%make_build

%install
%make install DESTDIR=%buildroot PREFIX=/usr
mkdir -p %buildroot%_sysconfdir/bash_completion.d
mv %buildroot%_datadir/bash_completion.d/nvme %buildroot%_sysconfdir/bash_completion.d/

%files
%doc *.md LICENSE
%_sbindir/nvme
%_man1dir/nvme*.1*
%_sysconfdir/bash_completion.d/nvme

%post
if [ $1 = 1 ]; then # 1 : This package is being installed for the first time
	if [ ! -f /etc/nvme/hostnqn ]; then
		install -D /dev/null /etc/nvme/hostnqn
		echo $(nvme gen-hostnqn) > /etc/nvme/hostnqn
        fi
        if [ ! -f /etc/nvme/hostid ]; then
                uuidgen > /etc/nvme/hostid
        fi
fi

%preun
if [ "$1" = "remove" ]; then
	if [ -d /etc/nvme ]; then
		rm -f /etc/nvme/hostnqn
		if [ ! -n "`ls -A /etc/nvme`" ]; then
			rm -rf /etc/nvme
		fi
	fi
fi
%changelog
* Thu Oct 05 2017 L.A. Kostis <lakostis@altlinux.ru> 1.4-alt2
- Rebuild with uuid support.
- Re-organize documentation.

* Thu Oct 05 2017 L.A. Kostis <lakostis@altlinux.ru> 1.4-alt1
- Initial build for ALTLinux.

* Thu Oct 15 2015 Keith Busch <keith.busch@intel.com>
- Initial RPM spec
