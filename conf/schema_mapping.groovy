mapping {
  map timestamp() onto 'timestamp'
  map eventParameter('username') onto 'user_id'
  map sessionId() onto 'sessionId'
  map eventParameter('queryString') onto 'raw_query'
  map eventParameter('p_m') onto 'p_m'
  map referer() onto 'url'
  map remoteHost() onto 'remoteHost'
  map location() onto 'location'
  map userAgentString() onto 'userAgentName'
  map pageViewId() onto 'page_id'
  map eventParameter('category_id') onto 'category_id'
  map eventParameter('partner_id') onto 'partner_id'
  map eventParameter('suspect') onto 'suspect'

  def locationUri = parse location() to uri
  def localUri = parse locationUri.rawFragment() to uri
  map localUri.path() onto 'ref_url'
  map eventType() onto 'eventType' 
"""  def localQuery = localUri.query()
  map localQuery.value('q') onto 'q'

   
  map { parse localQuery.value('n') to int32 } onto 'n'"""
}
