Name: msmtpqueue
Version: 0.5
Release: alt1

%define name0 msmtp

Summary: Queue mails offline and send them all at a later point with %name0
License: GPL
Group: Networking/Mail
Url: http://%name0.sourceforge.net
Source: http://mesh.dl.sourceforge.net/sourceforge/%name0/%name-%version.tar.gz

Summary(ru_RU.KOI8-R): Накопление и пакетная отправка отправляемой почты

Requires: %name0

%description
Scripts to queue mails and send them all at a later point with msmtp.

These scripts may be useful for dialup connections: You can "send" all your
mails offline (they will be queued by msmtp-enqueue.sh) and really send them
all later when you are online (by running msmtp-runqueue.sh).

%description -l ru_RU.KOI8-R
Данный пакет содержит два сценария, предназначенных для использования
на компьютерах с коммутируемым подключением к Интернету.

Первый из них, %name0-enqueue.sh, служит для замены /usr/sbin/sendmail
в качестве агента отправки почты (MDA, Mail Delivering Agent).
Вместо фактической отправки этот сценарий сохраняет почту во временном буфере,
где она будет находиться до тех пор, пока не будет вызван второй сценарий,
%name0-runqueue.sh, который отправляет накопившуюся в буфере почту наружу,
используя утилиту %name0.

Подключите первый сценарий к своей почтовой программе (например, к Mutt),
а второй - в сценарий, выполняемый при установке подключения к Интернету.

%prep
%setup -q

%build

%install
%__mkdir -p %buildroot%_bindir
%__install -p %name0-*.sh %buildroot%_bindir

%files
%_bindir/%name0-*.sh
%doc ChangeLog README

%changelog
* Mon May 14 2007 Ilya Evseev <evseev@altlinux.ru> 0.5-alt1
- updated to version 0.5

* Fri Feb 17 2006 Ilya Evseev <evseev@altlinux.ru> 0.4-alt1
- initial build for ALTLinux

## EOF ##
