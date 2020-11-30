# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name:	 getssl
Version: 2.31
Release: alt1

Summary: Obtain SSL certificates from the letsencrypt.org ACME server
License: GPL-3.0
Group: Networking/Other
Url: https://github.com/srvrco/getssl
Vcs: https://github.com/srvrco/getssl.git
Source: %name-%version.tar
BuildArch: noarch

# Why AutoReq did not notice curl?
Requires: curl

# Following tools are optional.
%filter_from_requires /\(mysql\|scp\|ssh\|xxd\|gettext\)/d

# getssl requires one of {dig,nslookup,drill,host}, but autoreq will
# notice bind-utils, thus 'host'.

%description
Obtain SSL certificates from the letsencrypt.org ACME server. Suitable for
automating the process on remote servers.

%prep
%setup

# /.out/getssl-2.31-alt1.noarch.rpm: forbidden requires: python-base
# sisyphus_check: check-deps ERROR: package dependencies violation
sed -i s/python/python3/ dns_scripts/dns_route53.py

%build

%install
%makeinstall_std install

%files
%doc LICENSE README.md
%_bindir/getssl
%_datadir/getssl

%changelog
* Mon Nov 30 2020 Vitaly Chikunov <vt@altlinux.org> 2.31-alt1
- First import of v2.31 (2020-11-29).
