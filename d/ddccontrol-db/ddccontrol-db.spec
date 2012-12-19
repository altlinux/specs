# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name ddccontrol-db
%define version 20061014
%global git_commit e8cc385a6321e7c99783150001193ec6e9e0c436
%global git_date 20120904

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

# git clone git://ddccontrol.git.sourceforge.net/gitroot/ddccontrol/ddccontrol-db
# cd ddccontrol-db
# git archive --format=tar --prefix=%%{name}-%%{version}/ %%{git_commit} | \
# bzip2 > ../%%{name}-%%{version}-%%{git_suffix}.tar.bz2

Name:             ddccontrol-db
URL:              http://ddccontrol.sourceforge.net/
Version:          20061014
Release:          alt1_3.20120904git%(echo e8cc385a6321e7c99783150001193ec6e9e0c436 | cut -c -8)
# Agreed by usptream to be GPLv2+
# http://sourceforge.net/mailarchive/message.php?msg_id=29762202
License:          GPLv2+
Group:            File tools
Summary:          DDC/CI control database for ddccontrol
#Source0:          http://downloads.sourceforge.net/ddccontrol/%{name}-%{version}.tar.bz2
Source0:          %{name}-%{version}-%{git_suffix}.tar.bz2
# use autopoint instead of gettextize that is interactive tool
Patch0:           %{name}-autopoint.patch
BuildRequires:    gettext gettext-devel libtool perl(XML/Parser.pm)
BuildArch:        noarch
Source44: import.info
# dell3011 https://bugzilla.altlinux.org/show_bug.cgi?id=27551
Patch33: ddccontrol-db-0.4.2-dell3011.patch
Patch34: ddccontrol-db-0.4.2-russian.patch
Conflicts: ddccontrol < 0.4.2-alt15

%description
DDC/CU control database for DDCcontrol.

%prep
%setup -q
%patch0 -p1 -b .autopoint
%patch34 -p2

./autogen.sh

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_datadir}/%{name}

%changelog
* Wed Dec 19 2012 Igor Vlasenko <viy@altlinux.ru> 20061014-alt1_3.20120904gite8cc385a
- fc import for more frequent updates

