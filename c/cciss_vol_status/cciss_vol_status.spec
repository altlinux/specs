Name: cciss_vol_status
Version: 1.09
Release: alt1

Summary: Show status of logical drives on HP Smart Array controllers and MSA1000
License: GPL
Group: System/Kernel and hardware

Url: http://cciss.sourceforge.net/#cciss_utils
Source: %name-%version.tar.gz
Packager: Michael A. Kangin <prividen@altlinux.org>

Summary(ru_RU.UTF-8): Отображение статуса дисков на контроллере Smart Array и MSA1000

%description
%name - a very lightweight program to report the status of logical
drives on HP Smart Array controllers and also fibre channel attached
MSA1000.

%prep
%setup
%autoreconf

%build
%configure
%make_build

%install
%makeinstall_std

%files 
%doc AUTHORS ChangeLog NEWS README 
%_bindir/*
%_man8dir/*

%changelog
* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 1.09-alt1
- NMU: 1.09 (thx fedorawatch)
- minor spec cleanup

* Sun Jan 10 2010 Michael A. Kangin <prividen@altlinux.org> 1.06-alt1
- New version

* Tue Oct 07 2008 Michael A. Kangin <prividen@altlinux.org> 1.03-alt1
- initial build

