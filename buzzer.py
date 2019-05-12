import wx

import sms

import news as tn

import webscrap as ws

import weather as tw


# Some classes to use for the notebook pages.  Obviously you would
# want to use something more meaningful for your application, these
# are just for illustration.

class PageOne(wx.Panel):
        def __init__( self, parent ):
                wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 450,600 ), style = wx.TAB_TRAVERSAL )
                
                bSizer2 = wx.BoxSizer( wx.VERTICAL )
                        
                self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"News Notifier", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText6.Wrap( -1 )
                self.m_staticText6.SetFont( wx.Font( 20, 71, 90, 90, False, "Arial Black" ) )
                
                bSizer2.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
                
                self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
                self.m_panel8.SetMinSize( wx.Size( -1,150 ) )
                self.m_panel8.SetMaxSize( wx.Size( -1,150 ) )
                
                gSizer1 = wx.GridSizer( 0, 2, 15, 0 )
                
                self.Mobile = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Mobile No.:", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.Mobile.Wrap( -1 )
                gSizer1.Add( self.Mobile, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
                
                self.phno = wx.TextCtrl( self.m_panel8, wx.ID_ANY, "+919999999999", wx.DefaultPosition, wx.DefaultSize, 0 )
                gSizer1.Add( self.phno, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
                
                self.m_staticText4 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Country:", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText4.Wrap( -1 )
                gSizer1.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
                
                countryChoices = [ u"India", u"Pakistan", u"US", u"UK", u"China", u"Germany" ]
                self.country = wx.ComboBox( self.m_panel8, wx.ID_ANY, u"India", wx.DefaultPosition, wx.DefaultSize, countryChoices, wx.CB_READONLY )
                self.country.SetSelection( 0 )
                gSizer1.Add( self.country, 0, wx.ALL, 5 )
                
                
                self.m_panel8.SetSizer( gSizer1 )
                self.m_panel8.Layout()
                gSizer1.Fit( self.m_panel8 )
                bSizer2.Add( self.m_panel8, 0, wx.ALL|wx.EXPAND, 5 )
                
                self.b_send = wx.Button( self, wx.ID_ANY, u"Send News", wx.DefaultPosition, wx.DefaultSize, 0 )
                bSizer2.Add( self.b_send, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM|wx.LEFT|wx.RIGHT|wx.TOP, 10 )
                
                self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
                bSizer2.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
                
                self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
                bSizer21 = wx.BoxSizer( wx.VERTICAL )
                
                self.m_staticText1 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Status:", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText1.Wrap( -1 )
                bSizer21.Add( self.m_staticText1, 0, wx.ALL, 5 )
                
                self.log = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP)
                bSizer21.Add( self.log, 1, wx.ALL|wx.EXPAND, 5 )
                
                
                self.m_panel9.SetSizer( bSizer21 )
                self.m_panel9.Layout()
                bSizer21.Fit( self.m_panel9 )
                bSizer2.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )
                
                
                self.SetSizer( bSizer2 )
                self.Layout()
                
                # Connect Events
                self.b_send.Bind( wx.EVT_BUTTON, self.send_news )
            
        def __del__( self ):
                pass
            
            
            # Virtual event handlers, overide them in your derived class
        def send_news( self, event ):
                send_text=tn.get_news(self.log)
                send_phno=self.phno.GetLineText(0)

                try:
                    sms.sms_send(send_phno,send_text)
                except:
                    self.log.AppendText('Error Occured. Ensure the following:\n1. The mobile should be registered and properly entered.\n2. Check proper internet connectivity\n3. The text may be too large\n\nIf problem persists, we regret and please contact admin.\n')
                else:
                    self.log.AppendText('News succesfully sent to :'+send_phno)
                finally:        
                    self.log.AppendText('\n\n'+'Buzzer v1.0'.center(50,'=')+'\n\n')
                        
class PageTwo(wx.Panel):
        def __init__( self, parent ):
                wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 450,600 ), style = wx.TAB_TRAVERSAL )
                
                bSizer2 = wx.BoxSizer( wx.VERTICAL )
                
                self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"WordOfTheDay", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText6.Wrap( -1 )
                self.m_staticText6.SetFont( wx.Font( 20, 71, 90, 90, False, "Arial Black" ) )
                
                bSizer2.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
                
                self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
                self.m_panel8.SetMinSize( wx.Size( -1,150 ) )
                self.m_panel8.SetMaxSize( wx.Size( -1,150 ) )
                
                gSizer1 = wx.GridSizer( 0, 2, 15, 0 )
                
                self.Mobile = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Mobile No.:", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.Mobile.Wrap( -1 )
                gSizer1.Add( self.Mobile, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
                
                self.phno = wx.TextCtrl( self.m_panel8, wx.ID_ANY, "+919999999999", wx.DefaultPosition, wx.DefaultSize, 0 )
                gSizer1.Add( self.phno, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
                
                self.m_staticText4 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Language:", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText4.Wrap( -1 )
                gSizer1.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
                
                countryChoices = [ u"English" ]
                self.country = wx.ComboBox( self.m_panel8, wx.ID_ANY, u"English", wx.DefaultPosition, wx.DefaultSize, countryChoices, wx.CB_READONLY )
                self.country.SetSelection( 0 )
                gSizer1.Add( self.country, 0, wx.ALL, 5 )
                
                
                self.m_panel8.SetSizer( gSizer1 )
                self.m_panel8.Layout()
                gSizer1.Fit( self.m_panel8 )
                bSizer2.Add( self.m_panel8, 0, wx.ALL|wx.EXPAND, 5 )
                
                self.b_send = wx.Button( self, wx.ID_ANY, u"Send Word", wx.DefaultPosition, wx.DefaultSize, 0 )
                bSizer2.Add( self.b_send, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM|wx.LEFT|wx.RIGHT|wx.TOP, 10 )
                
                self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
                bSizer2.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
                
                self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
                bSizer21 = wx.BoxSizer( wx.VERTICAL )
                
                self.m_staticText1 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Status:", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText1.Wrap( -1 )
                bSizer21.Add( self.m_staticText1, 0, wx.ALL, 5 )
                
                self.log = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP)
                bSizer21.Add( self.log, 1, wx.ALL|wx.EXPAND, 5 )
                
                
                self.m_panel9.SetSizer( bSizer21 )
                self.m_panel9.Layout()
                bSizer21.Fit( self.m_panel9 )
                bSizer2.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )
                
                
                self.SetSizer( bSizer2 )
                self.Layout()
                
                # Connect Events
                self.b_send.Bind( wx.EVT_BUTTON, self.send_word )
                
        def __del__( self ):
                pass
        
        
        # Virtual event handlers, overide them in your derived class
        def send_word( self, event ):
                send_text=ws.wordofday(self.log)
                send_phno=self.phno.GetLineText(0)
                try:
                        sms.sms_send(send_phno,send_text)
                except:
                        self.log.AppendText('Error Occured. Check proper internet connectivity\n\nIf problem persists, we regret and please contact admin.\n')
                else:
                        self.log.AppendText('\nWord succesfully sent to :'+send_phno)
                finally:        
                        self.log.AppendText('\n\n'+'Buzzer v1.0'.center(50,'=')+'\n\n')

class PageThree ( wx.Panel ):
        def __init__( self, parent ):
                wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 450,600 ), style = wx.TAB_TRAVERSAL )
                
                bSizer2 = wx.BoxSizer( wx.VERTICAL )
                
                self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"QuoteOfTheDay", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText6.Wrap( -1 )
                self.m_staticText6.SetFont( wx.Font( 20, 71, 90, 90, False, "Arial Black" ) )
                
                bSizer2.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
                
                self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
                self.m_panel8.SetMinSize( wx.Size( -1,150 ) )
                self.m_panel8.SetMaxSize( wx.Size( -1,150 ) )
                
                gSizer1 = wx.GridSizer( 0, 2, 15, 0 )
                
                self.Mobile = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Mobile No.:", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.Mobile.Wrap( -1 )
                gSizer1.Add( self.Mobile, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
                
                self.phno = wx.TextCtrl( self.m_panel8, wx.ID_ANY, "+919999999999", wx.DefaultPosition, wx.DefaultSize, 0 )
                gSizer1.Add( self.phno, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
                
                self.m_staticText4 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Language:", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText4.Wrap( -1 )
                gSizer1.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
                
                countryChoices = [ u"English" ]
                self.country = wx.ComboBox( self.m_panel8, wx.ID_ANY, u"English", wx.DefaultPosition, wx.DefaultSize, countryChoices, wx.CB_READONLY )
                self.country.SetSelection( 0 )
                gSizer1.Add( self.country, 0, wx.ALL, 5 )
                
                
                self.m_panel8.SetSizer( gSizer1 )
                self.m_panel8.Layout()
                gSizer1.Fit( self.m_panel8 )
                bSizer2.Add( self.m_panel8, 0, wx.ALL|wx.EXPAND, 5 )
                
                self.b_send = wx.Button( self, wx.ID_ANY, u"Send Quote", wx.DefaultPosition, wx.DefaultSize, 0 )
                bSizer2.Add( self.b_send, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM|wx.LEFT|wx.RIGHT|wx.TOP, 10 )
                
                self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
                bSizer2.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
                
                self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
                bSizer21 = wx.BoxSizer( wx.VERTICAL )
                
                self.m_staticText1 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Status:", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText1.Wrap( -1 )
                bSizer21.Add( self.m_staticText1, 0, wx.ALL, 5 )
                
                self.log = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP)
                bSizer21.Add( self.log, 1, wx.ALL|wx.EXPAND, 5 )
                
                
                self.m_panel9.SetSizer( bSizer21 )
                self.m_panel9.Layout()
                bSizer21.Fit( self.m_panel9 )
                bSizer2.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )
                
                
                self.SetSizer( bSizer2 )
                self.Layout()
                
                # Connect Events
                self.b_send.Bind( wx.EVT_BUTTON, self.send_quote )
                
        def __del__( self ):
                pass
        
        
        # Virtual event handlers, overide them in your derived class
        def send_quote( self, event ):
                send_text=ws.quoteofday(self.log)
                send_phno=self.phno.GetLineText(0)
                try:
                        sms.sms_send(send_phno,send_text)
                except:
                        self.log.AppendText('Error Occured. Check proper internet connectivity\n\nIf problem persists, we regret and please contact admin.\n')
                else:
                        self.log.AppendText('\nQuote succesfully sent to :'+send_phno)
                finally:        
                        self.log.AppendText('\n\n'+'Buzzer v1.0'.center(50,'=')+'\n\n')

class PageFour ( wx.Panel ):
        def __init__( self, parent ):
                wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 450,600 ), style = wx.TAB_TRAVERSAL )
                
                bSizer2 = wx.BoxSizer( wx.VERTICAL )
                
                self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Horoscope", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText6.Wrap( -1 )
                self.m_staticText6.SetFont( wx.Font( 20, 71, 90, 90, False, "Arial Black" ) )
                
                bSizer2.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
                
                self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
                self.m_panel8.SetMinSize( wx.Size( -1,150 ) )
                self.m_panel8.SetMaxSize( wx.Size( -1,150 ) )
                
                gSizer1 = wx.GridSizer( 0, 2, 15, 0 )
                
                self.Mobile = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Mobile No.:", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.Mobile.Wrap( -1 )
                gSizer1.Add( self.Mobile, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
                
                self.phno = wx.TextCtrl( self.m_panel8, wx.ID_ANY, "+919999999999", wx.DefaultPosition, wx.DefaultSize, 0 )
                gSizer1.Add( self.phno, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
                
                self.m_staticText4 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Language:", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText4.Wrap( -1 )
                gSizer1.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
                
                countryChoices = [u"Aries (Mar 21-Apr 19)",u"Taurus (Apr 20-May 20)",u"Gemini (May 21-Jun 20)",u"Cancer (Jun 21-Jul 22)",u"Leo (Jul 23-Aug 22)",u"Virgo (Aug 23-Sep 22)",u"Libra (Sep 23-Oct 22)",u"Scorpio (Oct 23-Nov 21)",u"Sagittarius (Nov 22-Dec 21)",u"Capricorn (Dec 22-Jan 19)",u"Aquarius (Jan 20-Feb 18)",u"Pisces (Feb 19-Mar 20)"]
                self.country = wx.ComboBox( self.m_panel8, wx.ID_ANY, u"Aries", wx.DefaultPosition, wx.DefaultSize, countryChoices, wx.CB_READONLY )
                self.country.SetSelection( 0 )
                gSizer1.Add( self.country, 0, wx.ALL, 5 )
                
                
                self.m_panel8.SetSizer( gSizer1 )
                self.m_panel8.Layout()
                gSizer1.Fit( self.m_panel8 )
                bSizer2.Add( self.m_panel8, 0, wx.ALL|wx.EXPAND, 5 )
                
                self.b_send = wx.Button( self, wx.ID_ANY, u"Send Horoscope", wx.DefaultPosition, wx.DefaultSize, 0 )
                bSizer2.Add( self.b_send, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM|wx.LEFT|wx.RIGHT|wx.TOP, 10 )
                
                self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
                bSizer2.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
                
                self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
                bSizer21 = wx.BoxSizer( wx.VERTICAL )
                
                self.m_staticText1 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Status:", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText1.Wrap( -1 )
                bSizer21.Add( self.m_staticText1, 0, wx.ALL, 5 )
                
                self.log = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP)
                bSizer21.Add( self.log, 1, wx.ALL|wx.EXPAND, 5 )
                
                
                self.m_panel9.SetSizer( bSizer21 )
                self.m_panel9.Layout()
                bSizer21.Fit( self.m_panel9 )
                bSizer2.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )
                
                
                self.SetSizer( bSizer2 )
                self.Layout()
                
                # Connect Events
                self.b_send.Bind( wx.EVT_BUTTON, self.send_horo )
                
        def __del__( self ):
                pass
        
        
        # Virtual event handlers, overide them in your derived class
        def send_horo( self, event ):
                zodiac = self.country.GetSelection()
                send_text=ws.horoscope(self.log,zodiac)
                send_phno=self.phno.GetLineText(0)
                try:
                        sms.sms_send(send_phno,send_text)
                except:
                        self.log.AppendText('Error Occured. Check proper internet connectivity\n\nIf problem persists, we regret and please contact admin.\n')
                else:
                        self.log.AppendText('\nHoroscope succesfully sent to :'+send_phno)
                finally:        
                        self.log.AppendText('\n\n'+'Buzzer v1.0'.center(50,'=')+'\n\n')

class PageFive ( wx.Panel ):
        def __init__( self, parent ):
                wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 450,600 ), style = wx.TAB_TRAVERSAL )
                
                bSizer2 = wx.BoxSizer( wx.VERTICAL )
                
                self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Weather", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText6.Wrap( -1 )
                self.m_staticText6.SetFont( wx.Font( 20, 71, 90, 90, False, "Arial Black" ) )
                
                bSizer2.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
                
                self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
                self.m_panel8.SetMinSize( wx.Size( -1,150 ) )
                self.m_panel8.SetMaxSize( wx.Size( -1,150 ) )
                
                gSizer1 = wx.GridSizer( 0, 2, 15, 0 )
                
                self.Mobile = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Mobile No.:", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.Mobile.Wrap( -1 )
                gSizer1.Add( self.Mobile, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
                
                self.phno = wx.TextCtrl( self.m_panel8, wx.ID_ANY, "+919999999999", wx.DefaultPosition, wx.DefaultSize, 0 )
                gSizer1.Add( self.phno, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
                
                self.m_staticText4 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Location:", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText4.Wrap( -1 )
                gSizer1.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
                
                self.locat = wx.TextCtrl( self.m_panel8, wx.ID_ANY, "", wx.DefaultPosition, wx.DefaultSize, 0 )
                gSizer1.Add( self.locat, 1, wx.ALL, 5 )
                
                self.m_panel8.SetSizer( gSizer1 )
                self.m_panel8.Layout()
                gSizer1.Fit( self.m_panel8 )
                bSizer2.Add( self.m_panel8, 0, wx.ALL|wx.EXPAND, 5 )
                
                self.b_send = wx.Button( self, wx.ID_ANY, u"Send Report", wx.DefaultPosition, wx.DefaultSize, 0 )
                bSizer2.Add( self.b_send, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM|wx.LEFT|wx.RIGHT|wx.TOP, 10 )
                
                self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
                bSizer2.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
                
                self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
                bSizer21 = wx.BoxSizer( wx.VERTICAL )
                
                self.m_staticText1 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Status:", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText1.Wrap( -1 )
                bSizer21.Add( self.m_staticText1, 0, wx.ALL, 5 )
                
                self.log = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP)
                bSizer21.Add( self.log, 1, wx.ALL|wx.EXPAND, 5 )
                
                
                self.m_panel9.SetSizer( bSizer21 )
                self.m_panel9.Layout()
                bSizer21.Fit( self.m_panel9 )
                bSizer2.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )
                
                
                self.SetSizer( bSizer2 )
                self.Layout()
                
                # Connect Events
                self.b_send.Bind( wx.EVT_BUTTON, self.send_weather )
                
        def __del__( self ):
                pass
        
        
        # Virtual event handlers, overide them in your derived class
        def send_weather( self, event ):
                locat = self.locat.GetLineText(0)
                tw.loc(self.log,locat)
                send_text=tw.get_data(self.log,locat)
                send_phno=self.phno.GetLineText(0)
                try:
                        sms.sms_send(send_phno,send_text)
                except:
                        self.log.AppendText('Error Occured. Check proper internet connectivity\n\nIf problem persists, we regret and please contact admin.\n')
                else:
                        self.log.AppendText('\nWeather succesfully sent to :'+send_phno)
                finally:        
                        self.log.AppendText('\n\n'+'Buzzer v1.0'.center(50,'=')+'\n\n')


class MainFrame(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = 'BUZZER v1.0 - SMS Notifier', pos = wx.DefaultPosition, size = wx.Size( 450,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        # Here we create a panel and a notebook on the panel
        p = wx.Panel(self)
        nb = wx.Notebook(p)

        # create the page windows as children of the notebook
        page1 = PageOne(nb)
        page2 = PageTwo(nb)
        page3 = PageThree(nb)
        page4 = PageFour(nb)
        page5 = PageFive(nb)

        # add the pages to the notebook with the label to show on the tab
        nb.AddPage(page1, "News")
        nb.AddPage(page2, "Word")
        nb.AddPage(page3, "Quote")
        nb.AddPage(page4, "Horoscope")
        nb.AddPage(page5, "Weather")

        # finally, put the notebook in a sizer for the panel to manage
        # the layout
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizerAndFit(sizer)


if __name__ == "__main__":
    app = wx.App()
    MainFrame(None).Show()
    app.MainLoop()
