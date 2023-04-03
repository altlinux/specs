%define _unpackaged_files_terminate_build 1
%def_with check

%define cgitrc cgitrc.example
%define cgit_data %_datadir/%name
%define cgit_script_path %prefix/libexec
%define cgit_script_name %name
%define cgit_httpd_conf %apache2_sites_available/%name.conf

Name: cgit
Version: 1.2.3
Release: alt1

Summary: A hyperfast web frontend for git repositories written in C
Url: https://git.zx2c4.com/cgit/
License: GPL-2
Group: Development/Tools

Source0: %name-%version.tar
Source1: submodules.tar
Source2: %cgitrc

BuildRequires(pre): rpm-macros-apache2
BuildRequires: libzip-devel
BuildRequires: libssl-devel
BuildRequires: liblua5.1-devel
BuildRequires: zlib-devel
BuildRequires: rpm-build-python3

# BuildRequires for documentation
BuildRequires: asciidoc-a2x
BuildRequires: asciidoc-latex

# BuildRequires for check
%if_with check
BuildRequires: lzip
BuildRequires: unzip
BuildRequires: tidy
BuildRequires: strace
%endif

%description
This is an attempt to create a fast web interface for the Git SCM, using a
built-in cache to decrease server I/O pressure.

%package apache2
Summary: Cgit config file for Apache2
Group: Development/Tools
BuildArch: noarch
Requires(pre): apache2-base
Requires(pre): %name

%description apache2
%summary

%prep
%setup -a1 

# Configure Makefile variables
cat << EOF | tee cgit.conf
CGIT_SCRIPT_PATH = %cgit_script_path
CGIT_SCRIPT_NAME = %cgit_script_name
CGIT_DATA_PATH = %cgit_data
prefix = %prefix
DESTDIR = %buildroot
docdir = %_docdir/%name-%version
EOF

# default httpd config
cat << EOF | tee httpd.conf
# cgid module is required to run the cgit binary
LoadModule cgid_module %apache2_moduledir/mod_cgid.so

Alias /cgit-data %cgit_data
<Directory "%cgit_data">
    Require all granted
</Directory>

# Path to cgit binary
ScriptAlias /cgit %cgit_script_path/%cgit_script_name

# Redirect from root to /cgit
# RedirectMatch permanent ^/$ /cgit
EOF

%build
%make_build

%install
%makeinstall_std install-man install-doc

# install example of cgitrc
install -pD %SOURCE2 %buildroot/%_sysconfdir/%cgitrc

# install httpd config file
mkdir -p %buildroot/%apache2_sites_available
install -Dp -m0644 httpd.conf %buildroot/%cgit_httpd_conf

%check
%make_build test

%files apache2
%cgit_httpd_conf

%files
%doc README* COPYING AUTHORS
%cgit_script_path/%cgit_script_name
%cgit_data/*
%_target_libdir_noarch/%name/*
%_man5dir/*
%_sysconfdir/%cgitrc

%changelog
* Sat Oct 01 2022 Alexandr Shashkin <dutyrok@altlinux.org> 1.2.3-alt1
- Initial build for sisyphus

