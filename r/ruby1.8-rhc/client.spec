%define ruby_major 1.8
%define orig_name rhc

Summary:       Multi-tenant cloud management system client tools
Name:          ruby%ruby_major-%orig_name
Version:       0.90.4
Release:       alt1
Group:         System/Servers
License:       MIT
URL:           http://openshift.redhat.com
Source0:       rhc-%version.tar
Patch0:        rhc-%version-%release.patch

BuildArch:     noarch

BuildRequires: rpm-build-ruby ruby%ruby_major-rake
Requires:      git

Conflicts:     %orig_name

%def_without doc

%if_with doc
BuildRequires: ruby%ruby_major-tool-rdoc
%endif

%description
Provides OpenShift client libraries

%package doc
Summary: Documentation files for %orig_name
Group: Documentation

%description doc
Documentation files for %orig_name

%prep
%setup -q -n %orig_name-%version
%patch -p1

%build
for f in bin/rhc-*
do
  ruby -c $f
done

for f in lib/*.rb
do
  ruby -c $f
done

%install
mkdir -p %buildroot%_man1dir
mkdir -p %buildroot%_man5dir

for f in man/*
do
  len=`expr length $f`
  section=`expr substr $f $len $len`
  cp $f "%buildroot/usr/share/man/man$section/"
done

mkdir -p %buildroot%_sysconfdir/openshift
cp conf/express.conf %buildroot%_sysconfdir/openshift/

mkdir -p %buildroot%_bindir
cp bin/* %buildroot%_bindir/

mkdir -p %buildroot%ruby_sitelibdir
cp lib/rhc-common.rb %buildroot%ruby_sitelibdir/

%if_with doc
%rdoc lib/
%endif

%files
%doc doc/USAGE.txt
%_bindir/rhc*
%_man1dir/rhc*
%_man5dir/express*
%ruby_sitelibdir/*
%config(noreplace) %_sysconfdir/openshift/express.conf

%if_with doc
%files doc
%ruby_ri_sitedir/RHC*
%endif

%changelog
* Sat Apr 14 2012 Evgeny Sinelnikov <sin@altlinux.ru> 0.90.4-alt1
- Update ruby-1.8 version for new release

* Wed Jan 18 2012 Evgeny Sinelnikov <sin@altlinux.ru> 0.85.1-alt1
- Update ruby-1.8 version for new release

* Fri Dec 16 2011 Evgeny Sinelnikov <sin@altlinux.ru> 0.84.2-alt1
- Initial ruby-1.8 version build for ALT Linux Sisyphus

