%define _unpackaged_files_terminate_build 1
%set_perl_req_method relaxed

Name: pve-doc-generator
Summary: Proxmox VE Documentation helpers
Version: 8.2.3
Release: alt1
License: AGPL-3.0+ and GFDL-1.3+
Group: Documentation
Url: https://git.proxmox.com/
Vcs: git://git.proxmox.com/git/pve-docs.git
Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64

Requires: asciidoc-a2x source-highlight xmlto

BuildRequires: perl(JSON.pm)
BuildRequires: pve-common pve-manager pve-firewall pve-ha-manager pve-container pve-qemu-server pve-guest-common proxmox-widget-toolkit-dev
BuildRequires: asciidoc-a2x source-highlight

%description
Tool to auto-generate various Proxmox VE Documentation files

#%%add_findreq_skiplist %%_datadir/pve-doc-generator/*.pl

%prep
%setup -q -n %name-%version
grep 'proxmox.com' * -rl | while read f; do
	sed -i 's|proxmox.com|basealt.ru|' $f
done
sed -i 's|{python}|python3|' asciidoc/*.conf

# rm -f getting-help.adoc howto-improve-pve-docs.adoc pve-package-repos.adoc pve-faq.adoc pve-installation.adoc pve-system-requirements.adoc translation.adoc pve-installation-media.adoc system-booting.adoc cpu-models.conf.adoc

%build
%make DOCRELEASE=%version asciidoc-pve

%install
#%%make_install DESTDIR=%%buildroot gen-install
mkdir -p %buildroot%_datadir/pve-doc-generator/asciidoc
cp *.adoc *.pl *.mk *.xml %buildroot%_datadir/pve-doc-generator/
cp asciidoc/*pve*.conf %buildroot%_datadir/pve-doc-generator/asciidoc/
install -pD -m755 asciidoc-pve %buildroot%_bindir/asciidoc-pve

%files
%doc debian/copyright
%_bindir/asciidoc-pve
%_datadir/pve-doc-generator

%changelog
* Thu Aug 29 2024 Andrew A. Vasilyev <andy@altlinux.org> 8.2.3-alt1
- 8.2.3

* Fri Mar 29 2024 Andrew A. Vasilyev <andy@altlinux.org> 8.1.5-alt1
- 8.1.5

* Wed Mar 13 2024 Andrew A. Vasilyev <andy@altlinux.org> 8.1.4-alt1
- 8.1.4

* Wed Feb 28 2024 Andrew A. Vasilyev <andy@altlinux.org> 8.1.3-alt1
- 8.1.3

* Wed Oct 25 2023 Andrew A. Vasilyev <andy@altlinux.org> 7.4.2-alt3
- remove BR: libpve-cluster-perl (Closes: #48151)

* Thu May 25 2023 Andrew A. Vasilyev <andy@altlinux.org> 7.4.2-alt2
- add copyright file

* Fri Mar 24 2023 Andrew A. Vasilyev <andy@altlinux.org> 7.4.2-alt1
- 7.4-2

* Mon Mar 20 2023 Andrew A. Vasilyev <andy@altlinux.org> 7.3.1-alt1
- 7.3-1

* Wed Nov 23 2022 Andrew A. Vasilyev <andy@altlinux.org> 7.2.5-alt1
- 7.2-5
- fix tests
- do not remove adoc files to build pve-qemu-server docs

* Thu May 05 2022 Andrew A. Vasilyev <andy@altlinux.org> 7.2.2-alt1
- 7.2-2

* Thu Mar 17 2022 Alexey Shabalin <shaba@altlinux.org> 7.1.2-alt1
- 7.1-2
- build pve-doc-generator as separated package

