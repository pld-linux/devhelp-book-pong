Summary:	DevHelp book: pong
Summary(pl):	Ksi±¿ka do DevHelp'a o pong
Name:		devhelp-book-pong
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/pong.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about pong

%description -l pl
Ksi±¿ka do DevHelp o pong

%prep
%setup -q -c pong -n pong

%build
mv -f book pong
mv -f book.devhelp pong.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/pong
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install pong.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install pong/* $RPM_BUILD_ROOT%{_prefix}/books/pong

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs
