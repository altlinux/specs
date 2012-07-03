%define _name quicktree

Name: cacti-plugin-%_name
Version: 0.2
Release: alt1

%define cactiplugindir %_datadir/cacti/plugins

Summary: QuickTree is a 'shopping basket' for cacti graphs

License: GPLv2+
Group: Monitoring

URL: http://wotsit.thingy.com/haj/cacti/quicktree-plugin.html
Source0: http://wotsit.thingy.com/haj/cacti/%_name-%version.zip

Requires: cacti
BuildArch: noarch

# Automatically added by buildreq on Thu May 13 2010
BuildRequires: unzip

%description
Quite often while looking at an issue, you find yourself switching
between a small set of graphs that relate to the problem, but not
necessarily to the same device - the server load, it's mail queue,
and the switch port, for example. QuickTree is a 'shopping basket'
for graphs - click the '+' icon next to a graph and it's added to the QuickTree page.
You can collect graphs from across your Cacti install very quickly.
If it turns out that the set of graphs will be useful in the future too,
you can save them as a normal Cacti graph tree, provided that you have permissions to do so.

Each user (with QuickTree permssions) gets their own QuickTree.

%prep
%setup -q -n %_name

%build

%install
mkdir -p %buildroot%cactiplugindir/%_name
cp -a * %buildroot%cactiplugindir/%_name/

%files
%cactiplugindir/*

%changelog
* Thu May 13 2010 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt1
- initial build
