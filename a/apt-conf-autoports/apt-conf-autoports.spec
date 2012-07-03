%define destbranch t6
Name: apt-conf-autoports
Summary: Autoports repository for %{destbranch}
Version: 1.0
Release: alt2

License: GPL
Group: System/Base

%description
%{summary}.
To update packages from %{summary}, 
uncomment /apt/sources.list.d/autoports.list, update the packages you want 
and comment /apt/sources.list.d/autoports.list back to prevent accidental
dist-upgrade.

%install
mkdir -p %buildroot%_sysconfdir/apt/{sources,vendors}.list.d
cat > %buildroot%_sysconfdir/apt/vendors.list.d/autoports.list <<'EOF'
simple-key "cronbuild" {
	Fingerprint "DE73F3444C163CCD751AC483B584C633278EB305";
	Name "Cronbuild Service <cronbuild@altlinux.org>";
}
EOF
cat > %buildroot%_sysconfdir/apt/sources.list.d/autoports.list <<'EOF'
#rpm [cronbuild] http://autoports.altlinux.org/pub/ALTLinux/autoports/%{destbranch}/ noarch autoports
#rpm [cronbuild] http://autoports.altlinux.org/pub/ALTLinux/autoports/%{destbranch}/ %{_arch} autoports
EOF

%files
%config %_sysconfdir/apt/vendors.list.d/autoports.list
%config %_sysconfdir/apt/sources.list.d/autoports.list

%changelog
* Sat Oct 29 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2
- marked as config

* Sat Oct 29 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1
- first build
